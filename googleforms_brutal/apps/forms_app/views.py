from collections import Counter

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FormCreateForm, QuestionFormSet
from .models import Answer, Form, Option, Question, Response


@login_required
def dashboard(request):
    forms = Form.objects.filter(owner=request.user).prefetch_related('responses', 'questions')
    return render(request, 'forms_app/dashboard.html', {'forms': forms})


@login_required
def form_create(request):
    if request.method == 'POST':
        form = FormCreateForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.owner = request.user
            form_instance.save()
            messages.success(request, 'Formulario creado. Ahora agrega preguntas.')
            return redirect('form_edit', pk=form_instance.pk)
    else:
        form = FormCreateForm()
    return render(request, 'forms_app/form_create.html', {'form': form})


@login_required
def form_edit(request, pk):
    form_instance = get_object_or_404(Form, pk=pk, owner=request.user)

    if request.method == 'POST':
        form_form = FormCreateForm(request.POST, instance=form_instance)
        question_formset = QuestionFormSet(request.POST, instance=form_instance)
        if form_form.is_valid() and question_formset.is_valid():
            form_form.save()
            question_formset.save()
            messages.success(request, 'Formulario actualizado correctamente.')
            return redirect('dashboard')
    else:
        form_form = FormCreateForm(instance=form_instance)
        question_formset = QuestionFormSet(instance=form_instance)

    return render(
        request,
        'forms_app/form_edit.html',
        {'form_form': form_form, 'question_formset': question_formset, 'form_instance': form_instance},
    )


@login_required
def option_manage(request, pk):
    form_instance = get_object_or_404(Form, pk=pk, owner=request.user)
    managed_questions = form_instance.questions.filter(question_type__in=[Question.SINGLE, Question.MULTIPLE])

    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        bulk_options = request.POST.get('bulk_options', '')
        question = get_object_or_404(Question, pk=question_id, form=form_instance)
        entries = [opt.strip() for opt in bulk_options.split(',') if opt.strip()]
        question.options.all().delete()
        Option.objects.bulk_create([Option(question=question, text=entry) for entry in entries])
        messages.success(request, f'Se guardaron {len(entries)} opciones para "{question.label}".')
        return redirect('option_manage', pk=form_instance.pk)

    return render(
        request,
        'forms_app/option_manage.html',
        {
            'form_instance': form_instance,
            'managed_questions': managed_questions,
        },
    )


def form_fill(request, pk):
    form_instance = get_object_or_404(Form.objects.prefetch_related('questions__options'), pk=pk, is_public=True)

    if request.method == 'POST':
        response = Response.objects.create(form=form_instance)
        for question in form_instance.questions.all():
            if question.question_type in [Question.SINGLE, Question.MULTIPLE]:
                selected = request.POST.getlist(f'question_{question.id}')
                if question.is_required and not selected:
                    response.delete()
                    messages.error(request, 'Responde todas las preguntas obligatorias.')
                    return redirect('form_fill', pk=pk)
                answer = Answer.objects.create(response=response, question=question)
                options = Option.objects.filter(id__in=selected, question=question)
                answer.selected_options.set(options)
            else:
                value = request.POST.get(f'question_{question.id}', '').strip()
                if question.is_required and not value:
                    response.delete()
                    messages.error(request, 'Responde todas las preguntas obligatorias.')
                    return redirect('form_fill', pk=pk)
                Answer.objects.create(response=response, question=question, value=value)

        messages.success(request, '¡Respuesta enviada con éxito!')
        return redirect('form_fill', pk=pk)

    return render(request, 'forms_app/form_fill.html', {'form_instance': form_instance})


@login_required
def form_analytics(request, pk):
    form_instance = get_object_or_404(Form.objects.prefetch_related('questions__options', 'responses__answers'), pk=pk, owner=request.user)
    total_responses = form_instance.responses.count()
    analytics = {}

    for question in form_instance.questions.all():
        if question.question_type in [Question.SINGLE, Question.MULTIPLE]:
            counter = Counter()
            answers = Answer.objects.filter(question=question).prefetch_related('selected_options')
            for answer in answers:
                for option in answer.selected_options.all():
                    counter[option.text] += 1
            analytics[question.id] = dict(counter)
        else:
            non_empty = Answer.objects.filter(question=question).exclude(value='').count()
            analytics[question.id] = {'respondidas': non_empty}

    return render(
        request,
        'forms_app/form_analytics.html',
        {
            'form_instance': form_instance,
            'total_responses': total_responses,
            'analytics': analytics,
        },
    )

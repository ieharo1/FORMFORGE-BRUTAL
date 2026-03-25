from django import forms
from django.forms import inlineformset_factory

from .models import Form, Option, Question


class FormCreateForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['title', 'description', 'is_public']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['label', 'question_type', 'is_required', 'order']


QuestionFormSet = inlineformset_factory(
    Form,
    Question,
    form=QuestionForm,
    extra=3,
    can_delete=True,
)


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text']

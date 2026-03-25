from django.contrib import admin
from .models import Answer, Form, Option, Question, Response


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'is_public', 'created_at')
    list_filter = ('is_public', 'created_at')
    search_fields = ('title',)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('label', 'form', 'question_type', 'is_required', 'order')
    list_filter = ('question_type', 'is_required')
    inlines = [OptionInline]


admin.site.register(Option)
admin.site.register(Response)
admin.site.register(Answer)

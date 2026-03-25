from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Form(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forms')
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    TEXT = 'text'
    LONG_TEXT = 'long_text'
    SINGLE = 'single'
    MULTIPLE = 'multiple'

    TYPES = [
        (TEXT, 'Texto corto'),
        (LONG_TEXT, 'Texto largo'),
        (SINGLE, 'Selección única'),
        (MULTIPLE, 'Selección múltiple'),
    ]

    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='questions')
    label = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, choices=TYPES, default=TEXT)
    is_required = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.form.title} - {self.label}'


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='responses')
    submitted_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    value = models.TextField(blank=True)
    selected_options = models.ManyToManyField(Option, blank=True)

from django.forms import ModelForm
from django import forms
from .models import *

class TodoForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'category', 'documentation', 'notes', 'important', 'development_url',]




# -*- coding: utf-8 -*-
from django import forms
from todo.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # On va gerer resolved a un autre endroit
        exclude = ('is_resolved',)

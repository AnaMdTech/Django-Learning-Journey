from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Write a task...',
                'class': 'todo-input',
                'autocomplete': 'off'
            })
        }

from django import forms
from .models import Job, Category

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'salary', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Description','style': 'resize: none;', 'cols': '50', 'rows': '10'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # This adds the default 'Select a category' option
        self.fields['category'].empty_label = "Select a category"

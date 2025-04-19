from django import forms
from .models import Book

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['title', 'author', 'description', 'published_date'] # or '__all__' to include all fields
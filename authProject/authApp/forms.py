from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

  class Meta:
    model = User
    fields = ['username', 'password', 'password_confirm']

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')

    # check if the password match
    if password and confirm_password and password != confirm_password:
      raise forms.ValidationError("Passwords do not match")

    return cleaned_data
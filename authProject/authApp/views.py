from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from .forms import RegisterForm

# Create your views here.
def register_view(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = User.objects.create_user(username=username, password=password)
      login(request, user)
      return redirect('home')
    else:
      form = RegisterForm()
      return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      next_url = request.GET.get('next') or request.POST.get('next') or 'home'
      return redirect(next_url)
    else:
      error_message = 'Invalid credentials'
  return render(request, 'accounts/login.html', {'error': error_message})

def logout_view(request):
  if request.method == 'POST':
    logout(request)
    return redirect('login')
  else:
    return redirect('home')

# Home View
# using decorators
@login_required
def home_view(request):
  pass
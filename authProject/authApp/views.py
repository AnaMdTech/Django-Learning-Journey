from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from .forms import RegisterForm

# Create your views here.
def register_view(request):
  pass

def login_view(request):
  pass

def logout_view(request):
  pass

# Home View
# using decorators
@login_required
def home_view(request):
  pass
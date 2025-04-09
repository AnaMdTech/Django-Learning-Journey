from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm
# from django.views import View
# from django.views.generic.base import TemplateView
from django.views.generic import ListView

def home(request):
    return render(request, 'jobs/home.html')

def add_job(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('job-list')
    return render(request, 'jobs/job_form.html', {'form': form})

# def job_list(request):
#     jobs = Job.objects.all()
#     return render(request, 'jobs/job_list.html', {'jobs': jobs})

class JobListView(ListView):
    model = Job # define the model
    template_name = "jobs/job_list.html" # define the template to use for the view
    context_object_name = "jobs" # define the variable to use in the template the default is object_list
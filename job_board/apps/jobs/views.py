from django.shortcuts import render, redirect
from .models import Job, Category
from .forms import JobForm

def home(request):
    return render(request, 'jobs/home.html')

def add_job(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('job-list')
    return render(request, 'jobs/job_form.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})
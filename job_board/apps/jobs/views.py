from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib import messages
# from django.views import View
# from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView

def home(request):
    return render(request, 'jobs/home.html')

# def add_job(request):
#     form = JobForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('job-list')
#     return render(request, 'jobs/job_form.html', {'form': form})

class JobCreateView(CreateView):
    model = Job
    form_class = JobForm
    success_url = reverse_lazy('job-list')
    # template_name = 'jobs/job_form.html' # dont need to explicitly define the template name cause the default is job_form --> <app>/<model>_<viewtype>.html

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.instance.title)

        # Check for duplicate book title by same user
        if Job.objects.filter(title=form.instance.title).exists():
            messages.error(self.request, "You've already added a book with this title.")
            return redirect("add-job")  # or back to form

        return super().form_valid(form)



# def job_list(request):
#     jobs = Job.objects.all()
#     return render(request, 'jobs/job_list.html', {'jobs': jobs})

class JobListView(ListView):
    model = Job # define the model
    template_name = "jobs/job_list.html" # dont need to explicitly define the template name cause the default is job_form --> <app>/<model>_<viewtype>.html
    context_object_name = "jobs" # define the variable to use in the template the default is object_list
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-job', views.JobCreateView.as_view(), name='add-job'),
    # path('job-list', views.job_list, name='job-list')
    path('job-list', views.JobListView.as_view(), name='job-list')
]

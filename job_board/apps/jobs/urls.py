from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job-list'),
    path('jobs/<slug:slug>/', views.job_detail, name='job-detail')
]

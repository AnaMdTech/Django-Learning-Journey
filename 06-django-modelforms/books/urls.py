from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('books/', views.book_list, name='book_list'),  # We’ll create this in the next step
]

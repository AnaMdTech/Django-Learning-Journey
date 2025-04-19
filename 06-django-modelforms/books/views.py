from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the book to the database
            return redirect('book_list')  # Redirect to a new page (we'll create this next)
    else:
        form = BookForm()

    return render(request, 'books/add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all() # Get all books from the database
    return render(request, 'books/book_list.html', {'books': books})
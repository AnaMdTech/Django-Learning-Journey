# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .forms import ReviewForm
from .models import Review

# Create your views here.

# class based view
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank-you")

#! function based view
# def review(request):
#     form = ReviewForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("thank-you")

#     return render(request, "reviews/review.html", {
#         "form": form
#     })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
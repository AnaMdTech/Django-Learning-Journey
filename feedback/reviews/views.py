# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ReviewForm
from .models import Review

# Create your views here.


def review(request):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("thank-you")

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
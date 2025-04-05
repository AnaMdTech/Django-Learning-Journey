from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def review(request):
  if request.method == 'POST':
    # Process the form data here
    entered_username = request.POST['username']
    print(entered_username)
    return HttpResponseRedirect('/thank-you')
  
  return render(request, 'reviews/review.html')

def thank_you(request):
  return render(request, 'reviews/thank_you.html')
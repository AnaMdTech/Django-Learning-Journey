from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.shortcuts import render

# Create your views here.
monthly_challenges = {
    "january": "Eat no meat for entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for entire month! -> october",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
        })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"""
    #     <ul>{list_items}</ul>
    # """

    # return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month < 0 or month > len(months):  # Handle invalid month numbers
        return HttpResponseNotFound("Invalid month number!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # return HttpResponseRedirect(redirect_path)
    return redirect(redirect_path) # Better than HttpResponseRedirect

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")

        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        return render(request, "404.html", status=404)

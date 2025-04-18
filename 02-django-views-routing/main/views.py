from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Django Views Routing!</h1>")

def about(request):
    return HttpResponse("<h1>About Page: This is a simple static view.</h1>")

def greet_user(request, name):
    return HttpResponse(f"<h1>Hello, {name.capitalize()}! 👋🏾</h1>")

from django.shortcuts import render

def project_index(request):
    return render(request, 'index.html')
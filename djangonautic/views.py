from django.http import HttpResponse
# import to render html
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')
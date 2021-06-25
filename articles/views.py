from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
    # retrieves all article objects
    articles = Article.objects.all().order_by('date')
    # creating a dictionary to send to template
    return render(request, 'articles/article_list.html', {'articles': articles})
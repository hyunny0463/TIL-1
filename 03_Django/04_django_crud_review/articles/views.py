from django.shortcuts import render
from .models import Article

def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    #1. 
    article = Article()
    article.title = title
    article.content = content
    article.save()
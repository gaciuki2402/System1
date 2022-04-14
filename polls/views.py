from urllib import request
from django.shortcuts import render
from .models import Post

def home(request):
    context={
        "posts":Post.objects.all()
    }
    return render(request, 'polls/home.html', context)

def about(request):
    return render(request, 'polls/about.html', {"title":"This is About Page"})
    

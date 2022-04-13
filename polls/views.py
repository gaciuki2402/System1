from urllib import request
from django.shortcuts import render

posts= [
    {
        "author":"Grace G",
        "title":"Polls Post 1",
        "content":"First Post Content",
        "date_posted":"February 24, 2022"
    },
    {
        "author":"Day Njau",
        "title":"Polls Post 2",
        "content":"Second Post Content",
        "date_posted":"December 20, 2012"   
    }
]

def home(request):
    context={
        "posts":posts
    }
    return render(request, 'polls/home.html', context)

def about(request):
    return render(request, 'polls/about.html', {"title":"This is About Page"})
    

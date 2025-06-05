from django.shortcuts import render, HttpResponse
from .models import TodoItem, BlogItem

def index(request):
    return render(request, "home.html")

def todo(request):
    items = TodoItem.objects.all()
    return render(request, "todo.html", {"todo": items})

def blog(request):
    items = BlogItem.objects.all()
    return render(request, "blog.html", {"blog": items})
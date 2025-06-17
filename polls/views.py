from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, HttpResponse
from .models import TodoItem, BlogItem, Note
from .serializers import NoteSerializer


def index(request):
    return render(request, "home.html")

def todo(request):
    items = TodoItem.objects.all()
    return render(request, "todo.html", {"todo": items})

def blog(request):
    items = BlogItem.objects.all()
    return render(request, "blog.html", {"blog": items})

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
    
    
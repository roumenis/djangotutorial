from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
class BlogItem(models.Model):
    blogTitle = models.CharField(max_length=200)
    blogText = models.TextField()
    
class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    background_color = models.CharField(max_length=35, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B')], default='A') 
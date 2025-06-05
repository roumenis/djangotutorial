from django.contrib import admin
from .models import TodoItem, BlogItem

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(BlogItem)

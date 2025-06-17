from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

from . import views

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path("", views.index, name="index"),
    path("todo/", views.todo, name="Todos"),
    path("blog/", views.blog, name="blogs"),
    path("api/", include(router.urls)),
]
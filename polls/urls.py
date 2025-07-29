from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from .views import NoteViewSet
from . import views
from .views.todos import TodosListView
from .views.notes import NoteListView, NoteCreateView
from .views.users import UserView

router = DefaultRouter() 
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path("", views.index, name="index"),
    path("todo/", views.todo, name="Todos"),
    path("blog/", views.blog, name="blogs"),
    path("api/", include(router.urls)),
    path("notes/list/", NoteListView.as_view(), name="note-list-create"),
    path("notes/create/", NoteCreateView.as_view(), name="note-create"),
    path("todos/list/", TodosListView.as_view(), name="todos-list"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserView.as_view(), name='user-detail'),
]

from rest_framework.generics import ListAPIView
from polls.models import TodoItem
from polls.serializers import TodoSerializer

class TodosListView(ListAPIView):
    serializer_class = TodoSerializer
    queryset = TodoItem.objects.all()

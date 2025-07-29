from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView
from polls.models import Note
from polls.serializers import NoteSerializer

@api_view(['GET', 'POST'])
def note_list_create(request):
    if request.method == 'GET':
        notes = Note.objects.all().order_by('-created_at')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class NoteListView(ListAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all().order_by('-created_at')
    # This view is open to all users
    permission_classes = [AllowAny]
    
class NoteCreateView(CreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    
class NoteDetailView(RetrieveDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
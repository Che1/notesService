from django.http.response import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from notes.models import Note
from notes.permisions import IsOwner

from notes.serializers import NoteSerializer


class NotesListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(owner=user)


class NotesDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    lookup_field = 'id'

    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NotesBySubjectView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        note = Note.objects.filter(subject=request.data['subject'], owner=self.request.user)
        serializer = NoteSerializer(note, many=True)
        return Response({"notes": serializer.data})

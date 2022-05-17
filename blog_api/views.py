from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


from blog.models import Note
from .serializers import note_created, note_to_json


class NoteListCreateAPIView(APIView):
    def get(self, request) -> Response:
        notes = Note.objects.all()
        return Response([note_to_json(obj) for obj in notes])

    def post(self, request: Request) -> Response:
        data = request.data
        note = Note(**data)

        note.save(force_insert=True)

        return Response(
            note_created(note),
            status=status.HTTP_201_CREATED
        )


class NoteDetailAPIView(APIView):
    def get(self, request, pk: int) -> Response:
        note = get_object_or_404(Note, pk=pk)

        return Response(note_to_json(note))

    def put(self, request, pk: int) -> Response:
        request_object = request.data
        note = Note.objects.get(pk=pk)
        note.title = request_object['title']
        note.message = request_object['message']
        note.save()

        return Response(note_to_json(note))

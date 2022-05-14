from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


from blog.models import Note


class NoteListCreateAPIView(APIView):
    def get(self, request) -> Response:
        temp_note = Note.objects.all()
        return Response(temp_note)

    def post(self, request: Request) -> Response:
        ...


class NoteDetailAPIView(APIView):
    def get(self, request):
        ...

    def put(self, request):
        ...
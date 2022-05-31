from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


from blog.models import Note
# from .serializers import note_created, note_to_json
from .serializers import NoteSerializer, NewNoteSerializer
from . import filters


# class NoteListCreateAPIView(APIView):
#     def get(self, request) -> Response:
#         notes = Note.objects.all()
#         return Response([note_to_json(obj) for obj in notes])
#
#     def post(self, request: Request) -> Response:
#         data = request.data
#         note = Note(**data)
#
#         note.save(force_insert=True)
#
#         return Response(
#             note_created(note),
#             status=status.HTTP_201_CREATED
#         )
#
#
# class NoteDetailAPIView(APIView):
#     def get(self, request, pk: int) -> Response:
#         note = get_object_or_404(Note, pk=pk)
#
#         return Response(note_to_json(note))
#
#     def put(self, request, pk: int) -> Response:
#         request_object = request.data
#         note = Note.objects.get(pk=pk)
#         note.title = request_object['title']
#         note.message = request_object['message']
#         note.save()
#
#         return Response(note_to_json(note))


class NoteListCreateAPIView(APIView):

    def get(self, request) -> Response:
        notes = Note.objects.all()
        serializer = NoteSerializer(instance=notes, many=True)

        return Response(data=serializer.data)

    def post(self, request: Request) -> Response:
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(author=request.user)

        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )


class NoteDetailAPIView(APIView):

    def get(self, request, pk: int) -> Response:

        note = Note.objects.get(pk=pk)
        serializer = NoteSerializer(instance=note)

        return Response(data=serializer.data)

    def put(self, request, pk: int) -> Response:
        note = Note.objects.get(pk=pk)

        serializer = NoteSerializer(instance=note, data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(data=serializer.data)


class PublicNoteListListAPIView(ListAPIView):
    """/notes/public/"""
    queryset = Note.objects.all()
    serializer_class = NewNoteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # return queryset.filter(public=True)

        return queryset \
            .filter(public=True) \
            .order_by("-create_at") \
            .select_related("author") \
            .prefetch_related("comments")

    # def filter_queryset(self, queryset):
    #     author_id = self.request.query_params.get("author_id")
    #     return filters.note_filter_by_author_id(queryset, author_id)

from rest_framework import serializers

from blog.models import Note, Comment


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ('author',)


def note_to_json(note) -> dict:
    return {
        "id": note.id,
        "title": note.title,
        "message": note.message,
        "public": note.public
    }


def note_created(note) -> dict:
    return {
        "id": note.id,
        "title": note.title,
        "message": note.message,
        "public": note.public,
        "create_at": note.create_at,
        "update_at": note.update_at,
    }


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class NewNoteSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ('author',)

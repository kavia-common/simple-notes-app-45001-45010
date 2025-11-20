from rest_framework import serializers
from .models import Note


# PUBLIC_INTERFACE
class NoteSerializer(serializers.ModelSerializer):
    """Serializer for the Note model used in CRUD endpoints."""
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

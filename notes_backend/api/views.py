from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def health(request):
    """Simple health check endpoint."""
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
class NoteViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """ViewSet providing CRUD operations for Note."""
    queryset = Note.objects.all().order_by('-updated_at', '-created_at')
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

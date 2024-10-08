from rest_framework import viewsets, permissions
from .models import Hashtag
from .serializers import HashtagSerializer

class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

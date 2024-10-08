from rest_framework import viewsets, permissions
from .models import Like
from .serializers import LikeSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save the like instance with the current user as the liker
        serializer.save(user=self.request.user)


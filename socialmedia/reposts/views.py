from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Repost
from .serializers import RepostSerializer

class RepostViewSet(viewsets.ModelViewSet):
    queryset = Repost.objects.all()  # Retrieve all reposts
    serializer_class = RepostSerializer  # Use the RepostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can perform actions

    def perform_create(self, serializer):
        # Automatically set the user when creating a repost
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the repost instance to delete
        if instance.user != request.user:
            # Check if the user trying to delete is the original user
            return Response({'error': 'You can only delete your own reposts.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)  # Delete the repost

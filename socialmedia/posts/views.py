from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from likes.models import Like  # Adjusted import
from likes.serializers import LikeSerializer  # Adjusted import

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-timestamp')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the authenticated user as the post's author
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # Check if the current user is the author of the post
        if instance.user != request.user:
            return Response({'error': 'You can only update your own posts.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Check if the current user is the author of the post
        if instance.user != request.user:
            return Response({'error': 'You can only delete your own posts.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)






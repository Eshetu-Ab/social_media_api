from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from likes.models import Like 
from likes.serializers import LikeSerializer 

class PostViewSet(viewsets.ModelViewSet):        # Defining a ViewSet for handling Post objects
    queryset = Post.objects.all().order_by('-timestamp') # The queryset to retrieve all Post objects, ordered by timestamp in descending order
    serializer_class = PostSerializer       # Specifying the serializer class to convert Post instances to JSON and vice versa
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Setting permission classes to allow authenticated users to edit, while unauthenticated users can only read

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






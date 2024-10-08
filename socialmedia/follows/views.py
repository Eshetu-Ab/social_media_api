from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Follow
from .serializers import FollowSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set follower to the authenticated user
        follower = self.request.user

        # Get the ID of the user to follow from the request data
        following_id = self.request.data.get('following')
        
        # Ensure that the following user exists
        try:
            following = User.objects.get(id=following_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Prevent a user from following themselves
        if follower == following:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save the follow relationship
        serializer.save(follower=follower, following=following)

    def destroy(self, request, *args, **kwargs):
        # Get the follow instance
        instance = self.get_object()

        # Only allow the authenticated user to unfollow users they are following
        if instance.follower != request.user:
            return Response({'error': 'You can only unfollow users you are following.'}, status=status.HTTP_403_FORBIDDEN)

        # Proceed with the unfollow operation
        return super().destroy(request, *args, **kwargs)


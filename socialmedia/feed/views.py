# feed/views.py
from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from posts.models import Post  # Import the Post model
from posts.serializers import PostSerializer  # Import the PostSerializer

# Custom pagination class to manage pagination in the feed
class FeedPagination(PageNumberPagination):
    page_size = 10  # Default number of items per page
    page_size_query_param = 'page_size'  # Allow the client to set page size
    max_page_size = 100  # Maximum allowed page size

class FeedView(generics.ListAPIView):
    """
    View to retrieve posts from users that the authenticated user is following.
    """
    serializer_class = PostSerializer  # Specify the serializer class to use
    permission_classes = [permissions.IsAuthenticated]  # Ensure user is authenticated
    pagination_class = FeedPagination  # Use custom pagination class
    filter_backends = [filters.OrderingFilter]  # Allow ordering of the results
    ordering_fields = ['timestamp', 'likes_count', 'comments_count', 'reposts_count']  # Fields that can be ordered
    ordering = ['-timestamp']  # Default ordering to reverse chronological order

    def get_queryset(self):
        """
        Override get_queryset to filter posts by the users the authenticated user is following.
        """
        user = self.request.user  # Get the currently authenticated user
        following_users = user.following.values_list('following', flat=True)  # Get the list of users being followed
        # Return posts from the followed users, ordered by timestamp in descending order
        return Post.objects.filter(user__in=following_users).order_by('-timestamp')

class CreatePostView(generics.CreateAPIView):
    """
    View for creating new posts.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user when creating a new post
        serializer.save(user=self.request.user)

# feed/urls.py
from django.urls import path
from .views import FeedView, CreatePostView  # Import both views

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),  # Base URL for getting the feed
    path('create/', CreatePostView.as_view(), name='create_post'),  # URL for creating new posts
]


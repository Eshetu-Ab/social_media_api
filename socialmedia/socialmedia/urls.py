"""
URL configuration for socialmedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# social_media_api/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # JWT Token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Admin
    path('admin/', admin.site.urls),

    # Include app URLs
    path('api/users/', include('users.urls')),          # User management and signup/login
    path('api/posts/', include('posts.urls')),          # Posts-related endpoints
    path('api/likes/', include('likes.urls')),          # Like system
    path('api/comments/', include('comments.urls')),    # Commenting system
    path('api/notifications/', include('notifications.urls')),  # Notifications
    path('api/direct_messages/', include('direct_messages.urls')),  # Messaging
    path('api/follows/', include('follows.urls')),      # Follows system
    path('api/hashtags/', include('hashtags.urls')),    # Hashtag system
    path('api/reposts/', include('reposts.urls')),      # Reposts
    path('api/feed/', include('feed.urls')),            # Social feed
]






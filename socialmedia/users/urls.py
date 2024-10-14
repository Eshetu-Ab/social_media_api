# users/urls.py
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView, UserViewSet
from rest_framework.routers import DefaultRouter

# Define router for API routes
router = DefaultRouter()
router.register(r'users', UserViewSet)

# Non-API routes for authentication (login, logout, signup)
auth_patterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

# Combine API and auth routes
urlpatterns = [
    path('', include(router.urls)),  # API routes
    path('', include(auth_patterns)),  # Authentication routes
]


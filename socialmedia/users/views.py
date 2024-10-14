from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages  # Import messages for feedback
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .models import CustomUser
from .serializers import UserSerializer
from .forms import CustomUserCreationForm  # Import  custom form

# View for user signup
class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # Use our custom form
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Check if the username or email already exists
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        
        if CustomUser.objects.filter(username=username).exists():
            form.add_error('username', 'Username already exists.')
            return self.form_invalid(form)

        if CustomUser.objects.filter(email=email).exists():
            form.add_error('email', 'Email already registered.')
            return self.form_invalid(form)

        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Successfully registered!")  # success message
        return redirect(self.success_url)

    def form_invalid(self, form):
        # Render the signup page again with the form errors and messages
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)
    
class UserPagination(PageNumberPagination):
    page_size = 10  # Set the default page size
    page_size_query_param = 'page_size'  # Allow clients to set page size
    max_page_size = 100  # Limit max page size
# UserViewSet for API
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = UserPagination  # Add pagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)  # Add filtering
    ordering_fields = '__all__'  # Allow ordering by any field
    ordering = ['id']  # Default ordering
        # Custom pagination class


    def get_queryset(self):
        queryset = super().get_queryset()
        # Example filtering by username (or any other field)
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(username__icontains=username)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)





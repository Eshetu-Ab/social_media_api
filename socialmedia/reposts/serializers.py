from rest_framework import serializers
from .models import Repost
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the custom user model

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model to return the username."""
    class Meta:
        model = User  # Use the custom user model
        fields = ['id', 'username']  # Include 'id' and 'username' fields

class RepostSerializer(serializers.ModelSerializer):
    """Serializer for the Repost model."""
    user = UserSerializer(read_only=True)  # Use the UserSerializer for the user field

    class Meta:
        model = Repost
        fields = ['id', 'user', 'original_post', 'timestamp']
        read_only_fields = ['user']  # Make 'user' read-only since it is set in the view

    def create(self, validated_data):
        """Set the user from the request context."""
        validated_data['user'] = self.context['request'].user  # Set user to the authenticated user
        return super().create(validated_data)  # Call the parent class's create method to save the repost

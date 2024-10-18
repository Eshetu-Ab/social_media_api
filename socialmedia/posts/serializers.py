from rest_framework import serializers
from .models import Post
from likes.models import Like  # Importing the Like model from the likes app

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model to convert it to and from JSON.
    """
    class Meta:
        model = Post  # Specify the Post model for serialization
        fields = [
            'id', 
            'content', 
            'timestamp', 
            'media', 
            'likes_count', 
            'comments_count', 
            'reposts_count', 
            'user'  # Include 'user' to show the author of the post
        ]
        read_only_fields = [
            'id', 
            'timestamp', 
            'likes_count', 
            'comments_count', 
            'reposts_count', 
            'user'  # Ensure 'user' is read-only to prevent clients from changing it
        ]  

class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model to handle likes on posts.
    """
    class Meta:
        model = Like  # Specify the Like model for serialization
        fields = ['id', 'post', 'user']  # Include relevant fields
        read_only_fields = ['user']  # User is read-only since it is automatically assigned

    def create(self, validated_data):
       
        user = self.context['request'].user  # Get the authenticated user from the request context
        like = Like.objects.create(user=user, **validated_data)  # Create a new like instance
        return like  # Return the created like instance

from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'timestamp']  # Use 'timestamp' instead of 'created_at'

        # Make 'user' a read-only field so it's not required in the request body
        read_only_fields = ['user']


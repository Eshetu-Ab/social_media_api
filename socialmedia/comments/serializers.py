# comments/serializers.py

from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'user', 'timestamp']
        read_only_fields = ['user', 'timestamp']  # Ensure 'user' is read-only

    def create(self, validated_data):
        # 'user' is already handled in the view, so no need to pass it here
        return Comment.objects.create(**validated_data)





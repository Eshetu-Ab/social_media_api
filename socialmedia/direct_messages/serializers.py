from rest_framework import serializers
from direct_messages.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp', 'is_read']
        read_only_fields = ['sender', 'timestamp', 'is_read']

    def validate(self, data):
        if data['receiver'] == self.context['request'].user:
            raise serializers.ValidationError("You cannot send a message to yourself.")
        return data

















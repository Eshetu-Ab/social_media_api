from rest_framework import viewsets, permissions
from .models import Message
from .serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Users can view messages where they are either the sender or receiver.
        """
        return Message.objects.filter(sender=self.request.user) | Message.objects.filter(receiver=self.request.user)

    def perform_create(self, serializer):
        """
        Set the sender as the currently authenticated user.
        """
        serializer.save(sender=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """
        Override destroy method to allow message deletion by the sender only.
        """
        message = self.get_object()

        if message.sender != request.user:
            return Response({"detail": "You can only delete messages you have sent."}, status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)














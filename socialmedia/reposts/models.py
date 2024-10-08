from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class Repost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who reposted
    original_post = models.ForeignKey(Post, related_name='reposts', on_delete=models.CASCADE)  # The original post being reposted
    timestamp = models.DateTimeField(auto_now_add=True)  # Time when the repost was created

    def __str__(self):
        return f'Repost of {self.original_post} by {self.user}'  # A string representation of the repost


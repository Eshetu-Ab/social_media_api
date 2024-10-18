from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='media/', blank=True, null=True)
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    reposts_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.content[:20]} by {self.user}'

    def update_likes_count(self):
        """Update likes count whenever a like is added or removed."""
        self.likes_count = self.likes.count()
        self.save()

class PostLike(models.Model):  
    user = models.ForeignKey(User, related_name='post_likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_likes', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user} likes {self.post}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.post.update_likes_count()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.post.update_likes_count()


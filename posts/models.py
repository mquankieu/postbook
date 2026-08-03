from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # Author: Links the post to a Django user. If the user is deleted, their posts are deleted too.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
    # Added title field (max 200 characters)
    title = models.CharField(max_length=200)

    # Post content field
    content = models.TextField()
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Newest posts appear first

    def __str__(self):
        return f"{self.title} (@{self.author.username})"
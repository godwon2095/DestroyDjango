from django.db import models
from django.urls import reverse

class Post(models.Model):
    class Meta:
        ordering = ['-created_at']
        
    title = models.CharField(max_length=200)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:show', args=[self.pk])
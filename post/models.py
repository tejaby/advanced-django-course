from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
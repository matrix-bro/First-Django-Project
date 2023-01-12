from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Post.objects.all() was returning Post object
    # With this, it returns only Post title
    def __str__(self):
        return self.title

    #redirecting after creating post here
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})       
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%d/%m/%Y/', blank=True)
    summary = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=100)
    publication_date = models.DateTimeField(default=datetime.now, blank=True)
    post_is_published = models.BooleanField()

    def __str__(self):
        return self.title

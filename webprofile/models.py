from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    lorem_ipsum = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
        "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim "
        "ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
        "aliquip ex ea commodo consequat. Duis aute irure dolor in "
        "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
        "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
        "culpa qui officia deserunt mollit anim id est laborum."
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='Lorem ipsum')
    image = models.ImageField(
        upload_to='images/%d/%m/%Y/', blank=True, null=True)
    summary = models.TextField(default=lorem_ipsum[:122] + '...')
    content = models.TextField(default=lorem_ipsum)
    category = models.CharField(max_length=100, default='test')
    publication_date = models.DateTimeField(default=datetime.now, blank=True)
    post_is_published = models.BooleanField()

    def __str__(self):
        return self.title

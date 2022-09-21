from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = ResizedImageField(
        size=[100, 100], crop=['middle', 'center'],
        upload_to='profile_image/%d/%m/%Y/', blank=True, null=True)
    cover_image = ResizedImageField(
        size=[300, 1000], crop=['middle', 'center'],
        upload_to='profile_cover_image/%d/%m/%Y/', blank=True, null=True)

    def __str__(self):
        return f'{User.username}_profile'

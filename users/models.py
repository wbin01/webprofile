from django.db import models


class FormUser(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    email = models.EmailField()  # username and password
    password = models.CharField(max_length=50)
    password_confirm = models.CharField(max_length=50)
    is_posts_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

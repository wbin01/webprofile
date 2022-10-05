from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
# pip install django-resized
# https://github.com/un1t/django-resized
# Options
#
# size - max width and height, for example [640, 480]
#
# crop - resize and crop.
#   ['top', 'left'] - top left corner,
#   ['middle', 'center'] - is center cropping,
#   ['bottom', 'right'] - crop right bottom corner.
#
# quality - quality of resized image 1..100
#
# keep_meta - keep EXIF and other metadata, default True
#
# force_format - force the format of the resized image,
#   available formats are the one supported by pillow, default to None


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    url_title = models.CharField(max_length=200, default='')
    image = ResizedImageField(  # models.ImageField
        size=[500, 300], crop=['middle', 'center'],
        upload_to='images/%d/%m/%Y/', blank=True, null=True)
    summary = models.TextField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    # new_tag = models.CharField(max_length=100)
    publication_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField()
    is_for_main_page = models.BooleanField(default=False)

    def __str__(self):
        return self.title

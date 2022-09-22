# Generated by Django 4.1.1 on 2022-09-22 00:37

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1500, 300], upload_to='profile_cover_image/%d/%m/%Y/'),
        ),
    ]

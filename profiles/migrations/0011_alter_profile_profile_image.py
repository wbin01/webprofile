# Generated by Django 4.1.1 on 2022-09-24 02:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_profile_delete_profilesettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[150, 150], upload_to='profile_image/%d/%m/%Y/'),
        ),
    ]

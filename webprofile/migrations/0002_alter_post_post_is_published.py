# Generated by Django 4.1.1 on 2022-09-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_is_published',
            field=models.BooleanField(),
        ),
    ]

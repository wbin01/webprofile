# Generated by Django 4.1.1 on 2022-09-12 20:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/')),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('publication_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('post_is_published', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

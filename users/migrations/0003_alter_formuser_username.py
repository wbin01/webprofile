# Generated by Django 4.1.1 on 2022-09-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_formuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formuser',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]

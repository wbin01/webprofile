# Generated by Django 4.1.1 on 2022-10-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webprofile', '0030_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='review_reason',
            field=models.TextField(blank=True, default='Sinalizado como sensível. Mais detalhes em breve.', null=True),
        ),
    ]
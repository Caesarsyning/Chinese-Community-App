# Generated by Django 4.0.6 on 2022-08-13 08:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resale', '0014_alter_comment_author_alter_comment_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='resale_like_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]

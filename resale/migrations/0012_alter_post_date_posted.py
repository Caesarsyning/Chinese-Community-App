# Generated by Django 4.0.6 on 2022-08-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resale', '0011_alter_comment_options_remove_comment_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

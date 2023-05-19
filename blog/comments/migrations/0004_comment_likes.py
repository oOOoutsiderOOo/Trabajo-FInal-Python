# Generated by Django 4.2 on 2023-05-19 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_email'),
        ('comments', '0003_rename_post_id_comment_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_likes', to='users.user'),
        ),
    ]

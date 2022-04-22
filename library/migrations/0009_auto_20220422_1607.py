# Generated by Django 3.2 on 2022-04-22 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0008_rename_active_post_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_post', to='auth.user'),
        ),
    ]

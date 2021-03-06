# Generated by Django 3.1.7 on 2021-11-18 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20211117_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article_comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 4.2 on 2024-07-15 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/blog/default.png', upload_to='blog/'),
        ),
    ]

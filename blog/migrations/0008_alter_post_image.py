# Generated by Django 4.0.4 on 2023-08-15 04:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]

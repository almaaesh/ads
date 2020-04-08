# Generated by Django 2.1.2 on 2020-03-26 23:04

from django.db import migrations, models
import post.validators


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20200326_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/', validators=[post.validators.validate_file_extension], verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='Slug En'),
        ),
    ]

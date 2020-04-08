# Generated by Django 2.1.2 on 2020-03-26 15:05

from django.db import migrations, models
import post.validators


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/', validators=[post.validators.validate_file_extension], verbose_name='Image'),
        ),
    ]

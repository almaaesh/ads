# Generated by Django 2.1.2 on 2020-03-30 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20200331_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug_ar',
            field=models.SlugField(blank=True, max_length=250, null=True, verbose_name='Slug Ar'),
        ),
    ]

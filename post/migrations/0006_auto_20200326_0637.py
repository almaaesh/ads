# Generated by Django 2.1.2 on 2020-03-26 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200326_0633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slug_en',
            new_name='slug',
        ),
    ]

# Generated by Django 2.1.2 on 2020-03-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20200326_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='show',
            field=models.BooleanField(default=True, verbose_name='show'),
        ),
    ]

# Generated by Django 2.1.2 on 2020-03-30 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_country_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.Country', verbose_name='Default country'),
        ),
    ]

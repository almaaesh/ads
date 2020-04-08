# Generated by Django 2.1.2 on 2020-03-26 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20200327_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductIamge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/', verbose_name='Image')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='post.Product', verbose_name='Product ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
    ]

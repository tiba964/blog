# Generated by Django 3.2.7 on 2021-09-19 19:10

import blogs.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image_about', models.FileField(blank=True, default='', upload_to='background/about/', validators=[blogs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='ContactBackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image_contact', models.FileField(blank=True, default='', upload_to='background/about/', validators=[blogs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='IndexBackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image_index', models.FileField(blank=True, default='', upload_to='background/about/', validators=[blogs.validators.validate_image_extension])),
            ],
        ),
    ]
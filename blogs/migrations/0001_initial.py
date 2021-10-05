# Generated by Django 3.2.7 on 2021-09-19 18:29

import blogs.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogBackgroundImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image_blog', models.FileField(blank=True, default='', upload_to='background/blogs/', validators=[blogs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='BlogDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_image_one', models.FileField(blank=True, default='', upload_to='background/stories_detail/', validators=[blogs.validators.validate_image_extension])),
                ('blog_image_two', models.FileField(blank=True, default='', upload_to='background/stories_detail/', validators=[blogs.validators.validate_image_extension])),
                ('blog_image_three', models.FileField(blank=True, default='', upload_to='background/stories_detail/', validators=[blogs.validators.validate_image_extension])),
                ('blog_date', models.DateField(blank=True, default=datetime.date.today)),
                ('blog_location', models.CharField(blank=True, default='', max_length=300)),
                ('blog_name', models.CharField(blank=True, default='', max_length=300)),
                ('blog_desc1', models.CharField(blank=True, default='', max_length=120)),
                ('blog_desc2', models.TextField(blank=True, default='', max_length=1000)),
                ('blog_desc3', models.TextField(blank=True, default='', max_length=1000)),
                ('blog_desc4', models.TextField(blank=True, default='', max_length=1000)),
                ('blog_desc5', models.TextField(blank=True, default='', max_length=1000)),
                ('blog_desc6', models.TextField(blank=True, default='', max_length=1000)),
                ('blog_desc7', models.TextField(blank=True, default='', max_length=1000)),
            ],
            options={
                'ordering': ['-blog_date'],
            },
        ),
    ]
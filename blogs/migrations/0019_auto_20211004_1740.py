# Generated by Django 3.2.7 on 2021-10-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0018_rename_blog_desc_insatll_3_blogdetail_blog_desc_insatll_package_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetail',
            name='blog_desc_insatll_package_4',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='blog_desc_insatll_package_5',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='blogdetail',
            name='blog_desc_insatll_package_6',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]

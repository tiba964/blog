# Generated by Django 3.2.7 on 2021-10-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0022_auto_20211004_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetail',
            name='note',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
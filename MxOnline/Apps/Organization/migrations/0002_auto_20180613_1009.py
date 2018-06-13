# Generated by Django 2.0.6 on 2018-06-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(max_length=200, upload_to='static/images/CourseOrg/images/%Y/%m', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(max_length=200, upload_to='static/images/Teacher/images/%Y/%m', verbose_name='封面图'),
        ),
    ]

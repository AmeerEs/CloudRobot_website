# Generated by Django 3.1.5 on 2021-06-01 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20210601_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snapshot',
            name='Image',
        ),
        migrations.AddField(
            model_name='snapshot',
            name='image',
            field=models.ImageField(blank=True, upload_to='snapshot_Image'),
        ),
    ]
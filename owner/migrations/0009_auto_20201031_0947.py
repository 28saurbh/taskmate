# Generated by Django 3.1.2 on 2020-10-31 04:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0008_auto_20201030_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturemodel',
            name='about_picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='profile_picture',
            field=models.ImageField(upload_to='images'),
        ),
    ]
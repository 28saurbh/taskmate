# Generated by Django 3.1.2 on 2020-10-30 05:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_auto_20201030_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillmodel',
            name='des',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

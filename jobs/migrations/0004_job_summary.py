# Generated by Django 2.2.15 on 2020-08-30 10:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200830_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='summary',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
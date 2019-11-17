# Generated by Django 2.2.6 on 2019-11-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0013_auto_20191110_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='url_discuss_event',
        ),
        migrations.AddField(
            model_name='event',
            name='url_discourse_event',
            field=models.URLField(blank=True, max_length=250, null=True, verbose_name='discourse URL'),
        ),
    ]
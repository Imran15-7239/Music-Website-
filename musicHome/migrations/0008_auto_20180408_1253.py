# Generated by Django 2.0.3 on 2018-04-08 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicHome', '0007_album_gnere'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='gnere',
        ),
        migrations.AddField(
            model_name='song',
            name='gnere',
            field=models.CharField(default='', max_length=50),
        ),
    ]

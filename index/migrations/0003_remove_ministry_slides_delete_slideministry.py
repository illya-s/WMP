# Generated by Django 5.0.2 on 2024-02-16 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_remove_ministry_songs_remove_songministry_songs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ministry',
            name='slides',
        ),
        migrations.DeleteModel(
            name='SlideMinistry',
        ),
    ]

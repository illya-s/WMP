# Generated by Django 5.0.2 on 2024-02-16 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_songministry_model_alter_songministry_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songministry',
            name='name',
        ),
    ]

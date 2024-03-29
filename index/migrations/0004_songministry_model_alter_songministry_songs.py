# Generated by Django 5.0.2 on 2024-02-16 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_remove_ministry_slides_delete_slideministry'),
    ]

    operations = [
        migrations.AddField(
            model_name='songministry',
            name='model',
            field=models.ForeignKey(blank=True, help_text='Программа', null=True, on_delete=django.db.models.deletion.CASCADE, to='index.ministry'),
        ),
        migrations.AlterField(
            model_name='songministry',
            name='songs',
            field=models.ForeignKey(blank=True, help_text='Песни', null=True, on_delete=django.db.models.deletion.CASCADE, to='index.song'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0008_auto_20210406_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouttracker',
            name='session_notes',
            field=models.TextField(blank=True, max_length=350),
        ),
    ]

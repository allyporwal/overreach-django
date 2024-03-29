# Generated by Django 3.1.7 on 2021-03-25 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('workout_tracker', '0004_workouttracker_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouttracker',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workouts', to='profiles.userprofile'),
        ),
    ]

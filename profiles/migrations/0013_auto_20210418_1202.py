# Generated by Django 3.1.7 on 2021-04-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20210414_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_payment',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='next_payment',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
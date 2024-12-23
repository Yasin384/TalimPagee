# Generated by Django 5.1.1 on 2024-11-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_attendance_gps_location_remove_class_students_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='achievements',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name='student',
            name='exp',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='is_leader',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='steps',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='streak_day',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

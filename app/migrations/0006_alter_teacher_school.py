# Generated by Django 5.1.1 on 2024-11-21 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_student_achievements_student_exp_student_is_leader_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school'),
        ),
    ]
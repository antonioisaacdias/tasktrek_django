# Generated by Django 5.2 on 2025-04-04 01:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_project_comments_alter_task_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='expires_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

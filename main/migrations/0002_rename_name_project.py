# Generated by Django 4.2.4 on 2024-01-06 11:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Name",
            new_name="Project",
        ),
    ]

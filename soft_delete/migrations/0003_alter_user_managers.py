# Generated by Django 5.0.3 on 2024-03-30 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("soft_delete", "0002_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
    ]

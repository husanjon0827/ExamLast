# Generated by Django 5.0.3 on 2024-03-30 13:25

import soft_delete.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("soft_delete", "0003_alter_user_managers"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", soft_delete.models.SoftDeleteUserManager()),
            ],
        ),
    ]

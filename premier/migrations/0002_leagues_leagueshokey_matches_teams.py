# Generated by Django 5.0.3 on 2024-03-29 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("premier", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Leagues",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                (
                    "cover",
                    models.ImageField(default="media/default.jpg", upload_to="media"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LeaguesHokey",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                (
                    "cover",
                    models.ImageField(default="media/default.jpg", upload_to="media"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Matches",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                (
                    "team_id",
                    models.ManyToManyField(related_name="matches", to="premier.team"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Teams",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("stadium", models.CharField(max_length=128)),
                (
                    "cover",
                    models.ImageField(default="media/default.jpg", upload_to="media"),
                ),
                (
                    "league_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        to="premier.leagues",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-21 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="otp",
            field=models.IntegerField(default=145567, max_length=10),
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("Commissioner", "Commissioner"),
                    ("Citizen", "Citizen"),
                    ("Inspector", "Inspector"),
                    ("SubInspector", "SubInspector"),
                    ("Constable", "Constable"),
                ],
                default="Citizen",
                max_length=100,
            ),
        ),
    ]

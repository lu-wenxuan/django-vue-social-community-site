# Generated by Django 4.2.3 on 2023-08-12 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_user_friends_friendshiprequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="friends_count",
            field=models.IntegerField(default=0),
        ),
    ]

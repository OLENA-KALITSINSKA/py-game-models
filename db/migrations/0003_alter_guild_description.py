# Generated by Django 4.0.2 on 2024-03-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_guild_alter_race_name_skill_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

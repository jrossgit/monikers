# Generated by Django 3.1.1 on 2022-04-07 15:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_game_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.UUIDField(default=uuid.UUID('814cce92-523c-4b73-8831-dfc58654601b'), primary_key=True, serialize=False, verbose_name='Game UUID'),
        ),
    ]

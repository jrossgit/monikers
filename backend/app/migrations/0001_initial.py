# Generated by Django 3.1.1 on 2022-01-08 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='Game UUID')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='Card UUID')),
                ('title_text', models.CharField(max_length=256)),
                ('help_text', models.CharField(blank=True, max_length=512, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.game')),
            ],
        ),
    ]

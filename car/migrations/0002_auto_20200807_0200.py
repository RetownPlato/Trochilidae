# Generated by Django 3.0.3 on 2020-08-07 02:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_check',
            name='id',
        ),
        migrations.AddField(
            model_name='car_check',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='Left blank', primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.0.3 on 2020-08-05 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20200805_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car_user',
            options={'ordering': ['date', 'id'], 'permissions': (('can_change_status', 'Set car status'),)},
        ),
    ]
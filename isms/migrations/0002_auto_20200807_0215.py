# Generated by Django 3.0.3 on 2020-08-07 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images_info',
            name='extension',
            field=models.CharField(choices=[('PNG', '.png'), ('JPEG', '.jpeg'), ('GIF', '.gif'), ('BMP', '.bmp')], max_length=4),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-31 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0024_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, default='avatars/pawn.png', null=True, upload_to='avatars'),
        ),
    ]

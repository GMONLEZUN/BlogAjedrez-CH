# Generated by Django 4.0.4 on 2022-05-31 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0025_alter_avatar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]

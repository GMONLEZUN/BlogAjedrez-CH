# Generated by Django 4.0.4 on 2022-05-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_post_contenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]

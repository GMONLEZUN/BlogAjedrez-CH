# Generated by Django 4.0.4 on 2022-05-27 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Posts', '0016_alter_postbio_content_commentgames'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentgames',
            name='commenter',
        ),
        migrations.AddField(
            model_name='commentgames',
            name='commenter_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

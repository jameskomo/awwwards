# Generated by Django 2.2.1 on 2019-05-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowawards', '0006_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='project_link',
            field=models.CharField(default=True, max_length=60),
            preserve_default=False,
        ),
    ]

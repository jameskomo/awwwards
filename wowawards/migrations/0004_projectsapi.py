# Generated by Django 2.2.1 on 2019-05-26 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_contact_information'),
        ('wowawards', '0003_auto_20190526_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsApi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=60)),
                ('project_description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('project_image', models.ImageField(default='default.jpeg', upload_to='images/')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
    ]

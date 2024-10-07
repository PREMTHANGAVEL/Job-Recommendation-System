# Generated by Django 4.2 on 2024-10-07 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('skills_required', models.JSONField()),
                ('experience_level', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('skills', models.JSONField()),
                ('experience_level', models.CharField(max_length=100)),
                ('desired_roles', models.JSONField()),
                ('locations', models.JSONField()),
                ('job_type', models.CharField(max_length=50)),
            ],
        ),
    ]

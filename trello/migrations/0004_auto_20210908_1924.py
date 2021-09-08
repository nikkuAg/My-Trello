# Generated by Django 3.2.6 on 2021-09-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0003_rename_maintainer_project_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
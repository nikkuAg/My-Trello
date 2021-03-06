# Generated by Django 3.2.6 on 2021-09-30 17:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0004_auto_20210908_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='comment',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='team_members',
            field=models.ManyToManyField(null=True, related_name='team_member', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2 on 2021-04-27 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_poll_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='bodyJson',
            field=models.JSONField(default={}),
        ),
    ]

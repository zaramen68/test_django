# Generated by Django 3.2 on 2021-04-28 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_alter_question_polls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='polls',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.poll'),
        ),
    ]

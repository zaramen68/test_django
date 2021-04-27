# Generated by Django 3.2 on 2021-04-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeOfBegin', models.DateTimeField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeQ', models.IntegerField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('bodyText', models.TextField()),
                ('bodyJson', models.JSONField()),
                ('polls', models.ManyToManyField(to='article.Poll')),
            ],
        ),
    ]
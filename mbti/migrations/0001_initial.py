# Generated by Django 5.0.4 on 2024-04-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('mbti', models.CharField(max_length=4)),
                ('quote', models.CharField(max_length=300)),
            ],
        ),
    ]

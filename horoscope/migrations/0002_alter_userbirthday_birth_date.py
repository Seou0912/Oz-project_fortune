# Generated by Django 5.0.4 on 2024-04-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbirthday',
            name='birth_date',
            field=models.DateField(),
        ),
    ]

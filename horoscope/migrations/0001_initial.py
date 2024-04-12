# Generated by Django 5.0.4 on 2024-04-12 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBirthday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(db_column='birthday')),
                ('zodiac_sign', models.CharField(max_length=10)),
                ('horoscope', models.TextField()),
            ],
        ),
    ]

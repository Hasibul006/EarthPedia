# Generated by Django 5.1.6 on 2025-05-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_remove_country_currencies'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]

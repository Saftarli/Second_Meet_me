# Generated by Django 5.0.4 on 2024-04-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('parameter', models.CharField(blank=True, default='', max_length=255)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('created_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

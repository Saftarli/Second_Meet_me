# Generated by Django 5.0.4 on 2024-04-29 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_delete_generalsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='This variable of the setting.', max_length=255, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=255, verbose_name='Description')),
                ('parameter', models.CharField(blank=True, default='', max_length=255, verbose_name='Parameter')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
            ],
            options={
                'verbose_name': 'General Setting',
                'verbose_name_plural': 'General Settings',
                'ordering': ('name',),
            },
        ),
    ]

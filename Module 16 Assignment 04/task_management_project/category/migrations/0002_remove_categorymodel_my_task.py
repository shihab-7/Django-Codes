# Generated by Django 5.0 on 2023-12-18 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorymodel',
            name='My_task',
        ),
    ]
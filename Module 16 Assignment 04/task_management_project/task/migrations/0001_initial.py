# Generated by Django 5.0 on 2023-12-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('task_Description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('Assigning_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

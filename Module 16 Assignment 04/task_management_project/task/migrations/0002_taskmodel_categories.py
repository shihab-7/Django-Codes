# Generated by Django 5.0 on 2023-12-18 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_categorymodel_my_task'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='categories',
            field=models.ManyToManyField(to='category.categorymodel'),
        ),
    ]

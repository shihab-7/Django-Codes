# Generated by Django 5.0 on 2023-12-27 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0005_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
    ]

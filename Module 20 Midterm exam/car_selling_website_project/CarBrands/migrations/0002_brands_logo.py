# Generated by Django 5.0 on 2023-12-27 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarBrands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company/'),
        ),
    ]
# Generated by Django 4.2.2 on 2023-07-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_location_alter_ad_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]

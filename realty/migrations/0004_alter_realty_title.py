# Generated by Django 4.1.7 on 2023-02-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0003_alter_realty_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realty',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

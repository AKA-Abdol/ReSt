# Generated by Django 4.1.7 on 2023-02-19 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_alter_realtor_hire_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='realtor',
            name='photo',
        ),
        migrations.AddField(
            model_name='realtor',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
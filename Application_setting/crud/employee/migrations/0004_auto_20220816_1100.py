# Generated by Django 3.2.10 on 2022-08-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_setting_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='setting_id',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='employee',
            name='setting_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

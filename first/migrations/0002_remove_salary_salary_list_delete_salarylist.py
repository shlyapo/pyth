# Generated by Django 4.0.5 on 2022-06-09 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='salary_list',
        ),
        migrations.DeleteModel(
            name='SalaryList',
        ),
    ]
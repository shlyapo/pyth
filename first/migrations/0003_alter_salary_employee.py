# Generated by Django 4.0.5 on 2022-06-09 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_remove_salary_salary_list_delete_salarylist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.employee'),
        ),
    ]

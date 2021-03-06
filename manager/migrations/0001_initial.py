# Generated by Django 4.0.5 on 2022-06-09 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_id', models.IntegerField()),
                ('emp_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_id', models.IntegerField(default=0)),
                ('sum', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TransMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.PositiveIntegerField(default=0)),
                ('date_of_trans', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='add money', max_length=300)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.company')),
            ],
        ),
    ]

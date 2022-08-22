# Generated by Django 4.0.4 on 2022-08-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='uploads/')),
                ('fname', models.CharField(max_length=100)),
                ('mname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('dob', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('dist', models.CharField(max_length=100)),
                ('edu', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('mark', models.IntegerField()),
                ('role', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('sal', models.IntegerField()),
            ],
        ),
    ]

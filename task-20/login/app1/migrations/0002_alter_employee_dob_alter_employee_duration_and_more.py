# Generated by Django 4.0.4 on 2022-08-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='duration',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-04-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofile',
            name='specialization',
            field=models.CharField(max_length=55),
        ),
    ]

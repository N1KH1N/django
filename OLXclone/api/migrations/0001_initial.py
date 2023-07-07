# Generated by Django 4.1.4 on 2023-01-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('purchase_year', models.CharField(max_length=200)),
                ('kmdriven', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]
# Generated by Django 4.1.4 on 2023-02-28 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=250)),
                ('publisher', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=220)),
                ('isbn', models.CharField(max_length=200)),
                ('published_date', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to='images')),
            ],
        ),
    ]

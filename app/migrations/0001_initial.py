# Generated by Django 4.1.7 on 2023-06-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('emailid', models.EmailField(default='', max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=100)),
                ('countryCode', models.CharField(max_length=100)),
            ],
        ),
    ]

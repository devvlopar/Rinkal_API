# Generated by Django 4.1.7 on 2023-03-03 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=70)),
                ('address', models.TextField(max_length=500)),
                ('mobile', models.CharField(max_length=15)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]

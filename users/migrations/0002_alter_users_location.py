# Generated by Django 4.0.1 on 2023-01-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='location',
            field=models.ManyToManyField(blank=True, null=True, to='users.Location'),
        ),
    ]
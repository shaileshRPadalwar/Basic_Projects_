# Generated by Django 3.1.6 on 2021-02-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]

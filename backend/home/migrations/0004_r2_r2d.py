# Generated by Django 2.2.12 on 2020-06-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200602_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='r2',
            name='r2d',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
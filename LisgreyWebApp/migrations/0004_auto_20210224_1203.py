# Generated by Django 3.1.5 on 2021-02-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LisgreyWebApp', '0003_auto_20210218_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=1000),
        ),
    ]
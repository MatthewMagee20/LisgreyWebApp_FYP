# Generated by Django 3.1.5 on 2021-02-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_menus', '0003_remove_fooditem_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='category',
            field=models.CharField(choices=[('Starter', 'Starter'), ('Main Course', 'Main Course'), ('Kiddie Menu', 'Kiddie Menu'), ('Side Order', 'Side Order'), ('Dessert', 'Dessert'), ('Drinks', 'Drinks')], default='Started', max_length=120),
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-24 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LisgreyWebApp', '0008_delete_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitem',
            name='basket',
        ),
        migrations.RemoveField(
            model_name='basketitem',
            name='menu_item',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='allergen',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='category',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
        migrations.RemoveField(
            model_name='takeawayorder',
            name='basket',
        ),
        migrations.RemoveField(
            model_name='takeawayorder',
            name='user',
        ),
        migrations.DeleteModel(
            name='Allergen',
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='BasketItem',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='FoodItem',
        ),
        migrations.DeleteModel(
            name='TakeawayOrder',
        ),
    ]
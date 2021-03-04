# Generated by Django 3.1.5 on 2021-02-24 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food_menus', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TakeawayOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='ABC', max_length=120, unique=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], default='Started', max_length=120)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='takeaway.basket')),
                ('user', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('basket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='takeaway.basket')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_menus.fooditem')),
            ],
        ),
    ]

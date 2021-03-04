# Generated by Django 3.1.5 on 2021-02-18 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LisgreyWebApp', '0002_takeawayorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takeawayorder',
            name='customer',
        ),
        migrations.AddField(
            model_name='takeawayorder',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=1000),
        ),
        migrations.AddField(
            model_name='takeawayorder',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

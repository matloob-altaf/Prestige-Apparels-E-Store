# Generated by Django 3.0.5 on 2020-05-08 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0021_auto_20200508_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='variations',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='Guest.Inventory'),
        ),
    ]
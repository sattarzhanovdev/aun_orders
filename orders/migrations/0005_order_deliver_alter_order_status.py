# Generated by Django 5.2.4 on 2025-08-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deliver',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='В ожидании'),
        ),
    ]

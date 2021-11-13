# Generated by Django 3.2.7 on 2021-11-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guild',
            name='admin_role_id',
        ),
        migrations.RemoveField(
            model_name='guild',
            name='dispute_channel_id',
        ),
        migrations.RemoveField(
            model_name='guild',
            name='trade_channel_id',
        ),
        migrations.AlterField(
            model_name='guild',
            name='guild_balance',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='guild',
            name='total_fee_collected',
            field=models.BigIntegerField(default=0),
        ),
    ]
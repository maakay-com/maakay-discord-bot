# Generated by Django 3.2.7 on 2021-11-15 06:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211113_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildTransaction',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAW', 'Withdraw')], max_length=255)),
                ('amount', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('guild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.guild')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.transaction')),
                ('withdrawn_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
    ]
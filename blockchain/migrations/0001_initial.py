# Generated by Django 3.2.3 on 2021-06-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='block',
            fields=[
                ('hash_pointer', models.CharField(blank=True, max_length=256)),
                ('id', models.CharField(blank=True, max_length=256, primary_key=True, serialize=False)),
                ('Nonce', models.CharField(blank=True, max_length=256)),
                ('timestamp', models.DateTimeField(blank=True)),
                ('number_of_transactions', models.IntegerField(blank=True, default=0)),
                ('index', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'db_table': 'block',
            },
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(blank=True, max_length=256)),
                ('receiver', models.CharField(blank=True, max_length=256)),
                ('timestamp', models.DateTimeField(blank=True)),
                ('amount', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'db_table': 'transaction',
            },
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-30 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blockchain',
            old_name='last_hash',
            new_name='hash_pointer',
        ),
        migrations.AddField(
            model_name='blockchain',
            name='number_of_transactions',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

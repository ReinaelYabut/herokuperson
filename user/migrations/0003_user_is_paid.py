# Generated by Django 4.2.7 on 2024-02-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_tc'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
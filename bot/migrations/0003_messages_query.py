# Generated by Django 2.1.7 on 2019-03-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_remove_messages_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='query',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
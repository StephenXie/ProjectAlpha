# Generated by Django 3.1.4 on 2021-04-04 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todoitem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]

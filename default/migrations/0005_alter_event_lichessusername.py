# Generated by Django 3.2.8 on 2022-01-14 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0004_event_lichessusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lichessusername',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]

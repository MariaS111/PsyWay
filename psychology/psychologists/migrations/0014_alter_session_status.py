# Generated by Django 4.2 on 2023-05-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologists', '0013_alter_session_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='status',
            field=models.CharField(choices=[('await confirmation', 'Waiting for confirmation'), ('await', 'Await'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='await confirmation', max_length=20),
        ),
    ]

# Generated by Django 4.2 on 2023-05-01 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologists', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychologist',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='psychologist',
            name='password',
            field=models.CharField(default=123, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='psychologist',
            name='profile_image',
            field=models.ImageField(blank=True, default='psychologists_profile_images/prof_im.png', upload_to='psychologists_profile_images/'),
        ),
    ]

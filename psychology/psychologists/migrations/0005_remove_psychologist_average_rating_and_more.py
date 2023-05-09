# Generated by Django 4.2 on 2023-05-03 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('psychologists', '0004_alter_psychologist_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psychologist',
            name='average_rating',
        ),
        migrations.RemoveField(
            model_name='psychologist',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='psychologist',
            name='profile_image',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('specialization', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('profile_image', models.ImageField(blank=True, default='psychologists_profile_images/prof_im.png', upload_to='psychologists_profile_images/')),
                ('ps', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='psychologists.psychologist')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('rating', models.IntegerField()),
                ('psychologist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psychologists.psychologist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

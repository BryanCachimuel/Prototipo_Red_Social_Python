# Generated by Django 4.0.5 on 2022-06-30 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocialdj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='batman.png', upload_to=''),
        ),
    ]

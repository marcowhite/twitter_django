# Generated by Django 4.0.1 on 2022-01-07 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jitterprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jitterprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

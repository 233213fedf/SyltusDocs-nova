# Generated by Django 5.0.2 on 2024-03-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]

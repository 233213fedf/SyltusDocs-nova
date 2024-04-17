# Generated by Django 5.0.2 on 2024-03-13 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_alter_article_attachment_alter_article_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='名称')),
                ('file', models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='文件')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='attachment',
        ),
        migrations.AddField(
            model_name='article',
            name='attachment',
            field=models.ManyToManyField(to='docs.attach', verbose_name='__'),
        ),
    ]
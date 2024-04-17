# Generated by Django 5.0.2 on 2024-03-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0006_alter_attach_options_alter_article_attachment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='attachment',
            field=models.ManyToManyField(blank=True, to='docs.attach', verbose_name='附件'),
        ),
        migrations.AlterField(
            model_name='attach',
            name='file',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='文件'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-13 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='categoty',
            options={'verbose_name': '类目', 'verbose_name_plural': '类目'},
        ),
        migrations.AlterModelOptions(
            name='column',
            options={'verbose_name': '板块', 'verbose_name_plural': '板块'},
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'verbose_name': '分册', 'verbose_name_plural': '分册'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='cat',
        ),
        migrations.AlterField(
            model_name='article',
            name='col',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.column', verbose_name='板块'),
        ),
        migrations.AlterField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.issue', verbose_name='期号'),
        ),
        migrations.AlterField(
            model_name='column',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.categoty', verbose_name='所属'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.categoty', verbose_name='所属'),
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
    ]
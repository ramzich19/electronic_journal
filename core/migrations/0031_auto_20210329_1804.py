# Generated by Django 3.1.5 on 2021-03-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_remove_articles_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='docs',
            field=models.FileField(blank=True, null=True, upload_to='static/docs', verbose_name='Docs'),
        ),
        migrations.AddField(
            model_name='articles',
            name='docs2',
            field=models.FilePathField(null=True, path='media/document', recursive=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='filename',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
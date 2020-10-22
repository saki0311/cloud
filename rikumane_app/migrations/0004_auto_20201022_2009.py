# Generated by Django 3.0.8 on 2020-10-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rikumane_app', '0003_auto_20201022_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Image',
            field=models.ImageField(null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='account',
            name='MemoAnalysis',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='account',
            name='MemoES',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='event',
            name='Address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='Flow',
            field=models.BooleanField(default=True),
        ),
    ]
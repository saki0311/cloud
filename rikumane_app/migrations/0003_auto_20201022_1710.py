# Generated by Django 3.0.8 on 2020-10-22 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rikumane_app', '0002_auto_20201020_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='es',
            name='Company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rikumane_app.Company'),
        ),
        migrations.AlterField(
            model_name='event',
            name='Company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rikumane_app.Company'),
        ),
    ]

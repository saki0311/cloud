# Generated by Django 3.0.8 on 2020-10-19 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(max_length=200)),
                ('CompanyName', models.CharField(max_length=100)),
                ('LoginId', models.CharField(max_length=100)),
                ('Memo', models.CharField(default='', max_length=500)),
                ('Rate', models.IntegerField(default=0)),
                ('Account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rikumane_app.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=100)),
                ('EventStart', models.DateTimeField()),
                ('EventEnd', models.DateTimeField()),
                ('Flow', models.BooleanField(default=False)),
                ('Complete', models.BooleanField(default=False)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rikumane_app.Company')),
            ],
        ),
        migrations.CreateModel(
            name='ES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuestionTitle', models.CharField(max_length=100)),
                ('TextCounts', models.IntegerField(default=0)),
                ('QuestionContents', models.CharField(default='', max_length=1000)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rikumane_app.Company')),
            ],
        ),
    ]

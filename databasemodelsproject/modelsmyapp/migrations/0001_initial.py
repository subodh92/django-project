# Generated by Django 2.1.3 on 2018-11-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('eaddr', models.CharField(max_length=100)),
                ('emob', models.CharField(max_length=11)),
                ('esal', models.FloatField()),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='Voters_photos')),
                ('gender', models.IntegerField()),
                ('dob', models.DateField()),
                ('mobileno', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]

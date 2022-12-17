# Generated by Django 4.1.4 on 2022-12-16 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15, verbose_name='Name')),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]

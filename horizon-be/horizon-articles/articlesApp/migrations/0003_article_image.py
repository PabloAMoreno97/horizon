# Generated by Django 4.1.4 on 2022-12-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articlesApp', '0002_article_description_alter_article_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.CharField(default=0, max_length=1000, verbose_name='Image'),
            preserve_default=False,
        ),
    ]

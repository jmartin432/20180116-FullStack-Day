# Generated by Django 2.0.3 on 2018-03-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0002_shorturl_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

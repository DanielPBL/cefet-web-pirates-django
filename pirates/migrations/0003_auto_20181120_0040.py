# Generated by Django 2.1.3 on 2018-11-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirates', '0002_auto_20181120_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesouro',
            name='img_tesouro',
            field=models.ImageField(upload_to='imgs'),
        ),
    ]

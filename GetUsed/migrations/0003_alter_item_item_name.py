# Generated by Django 3.2 on 2021-11-18 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetUsed', '0002_auto_20211118_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='name'),
        ),
    ]

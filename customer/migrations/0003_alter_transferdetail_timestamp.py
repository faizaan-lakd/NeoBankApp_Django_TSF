# Generated by Django 3.2.4 on 2021-07-15 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210715_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferdetail',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

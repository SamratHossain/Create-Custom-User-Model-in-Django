# Generated by Django 3.1.7 on 2021-08-18 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210818_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='dateofbirth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='joinat',
            field=models.DateField(auto_now_add=True),
        ),
    ]
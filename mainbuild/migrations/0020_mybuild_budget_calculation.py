# Generated by Django 3.2.2 on 2021-08-20 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbuild', '0019_auto_20210820_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybuild',
            name='budget_calculation',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

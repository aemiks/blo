# Generated by Django 3.2.2 on 2021-08-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbuild', '0013_auto_20210718_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybuild',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y/%m%d', verbose_name='Poglądowe zdjęcie budowy'),
        ),
    ]

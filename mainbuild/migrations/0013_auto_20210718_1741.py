# Generated by Django 3.2.2 on 2021-07-18 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainbuild', '0012_auto_20210718_1734'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BuildStage',
        ),
        migrations.DeleteModel(
            name='BuildStageElement',
        ),
    ]
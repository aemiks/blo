# Generated by Django 3.2.2 on 2021-06-29 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainbuild', '0005_auto_20210629_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mybuilddescription',
            name='build',
        ),
        migrations.AddField(
            model_name='mybuild',
            name='description',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainbuild.mybuilddescription'),
        ),
    ]

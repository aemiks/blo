# Generated by Django 3.2.2 on 2021-08-06 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buildstages', '0009_alter_buildstageelement_stage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildstageelement',
            name='stage_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buildstages.buildstage'),
        ),
    ]
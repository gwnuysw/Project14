# Generated by Django 2.1 on 2018-08-14 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_treeindex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treeindex',
            name='ancester',
            field=models.IntegerField(null=True),
        ),
    ]

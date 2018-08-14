# Generated by Django 2.1 on 2018-08-14 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180814_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SecoundIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=20)),
                ('ancester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.FirstIndex')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsubtitle', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=2000, null=True)),
                ('ancester_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.SecoundIndex')),
            ],
        ),
        migrations.DeleteModel(
            name='TreeIndex',
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-22 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrashCan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tc_town_num', models.IntegerField(null=True)),
                ('tc_town', models.CharField(default='NoInput', max_length=32, null=True)),
                ('tc_road', models.CharField(default='NoInput', max_length=128, null=True)),
                ('tc_loc', models.CharField(default='NoInput', max_length=128, null=True)),
                ('tc_lat', models.CharField(max_length=100, null=True)),
                ('tc_lng', models.CharField(max_length=100, null=True)),
                ('tc_desc', models.CharField(default='NoInput', max_length=256, null=True)),
                ('tc_phone', models.CharField(max_length=48, null=True)),
                ('tc_link', models.URLField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.trashcan')),
            ],
        ),
    ]

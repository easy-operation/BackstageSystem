# Generated by Django 2.0.2 on 2018-03-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('password', models.CharField(max_length=15)),
                ('hostname', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('cpu_thread', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=15, null=True)),
                ('system_version', models.CharField(blank=True, max_length=30, null=True)),
                ('disk', models.CharField(blank=True, max_length=30, null=True)),
                ('memory', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

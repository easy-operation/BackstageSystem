# Generated by Django 2.0.2 on 2018-03-05 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VMManagement', '0004_auto_20180305_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serverinfo',
            old_name='memory',
            new_name='total_memory',
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='used_memory',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

# Generated by Django 3.0 on 2021-02-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210203_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeestockkeymap',
            old_name='issue',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='laptop',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='is_alloted',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='modems',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='tools',
        ),
        migrations.AddField(
            model_name='stock',
            name='no_of_items',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

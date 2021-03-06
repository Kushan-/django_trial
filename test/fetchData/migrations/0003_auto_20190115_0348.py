# Generated by Django 2.1.4 on 2019-01-15 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetchData', '0002_auto_20190112_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogsdata',
            name='guard_or_trained',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], max_length=1, null='no'),
        ),
        migrations.AlterField(
            model_name='dogsdata',
            name='spayed_or_neutered',
            field=models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='yes', max_length=1),
        ),
    ]

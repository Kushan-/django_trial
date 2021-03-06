# Generated by Django 2.1.4 on 2019-01-12 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DogsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dog_name', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('breed', models.CharField(blank=True, max_length=30)),
                ('birth', models.DateTimeField()),
                ('dominant_color', models.CharField(max_length=20)),
                ('secondary_color', models.CharField(blank=True, max_length=20)),
                ('third_color', models.CharField(blank=True, max_length=20)),
                ('spayed_or_neutered', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=1, null=True)),
                ('guard_or_trained', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=1, null=True)),
                ('borough', models.CharField(blank=True, default='n/a', max_length=30)),
                ('zip_code', models.IntegerField()),
            ],
        ),
    ]

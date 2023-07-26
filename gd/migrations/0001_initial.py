# Generated by Django 4.2.3 on 2023-07-25 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('score', models.DecimalField(decimal_places=2, max_digits=20)),
                ('current_rank', models.IntegerField()),
                ('max_rank', models.IntegerField()),
                ('registration_date', models.DateField(verbose_name='Registation date')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('length', models.DurationField()),
                ('status', models.CharField(max_length=50, verbose_name='On of several statuses')),
                ('publication_time', models.DateTimeField()),
                ('music', models.URLField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gd.player')),
            ],
        ),
    ]

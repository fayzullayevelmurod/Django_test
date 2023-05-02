# Generated by Django 4.2 on 2023-05-01 09:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('maximum_attemps', models.PositiveBigIntegerField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2023, 5, 11, 9, 53, 35, 721910, tzinfo=datetime.timezone.utc))),
                ('pass_parcentage', models.PositiveBigIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('a', models.CharField(max_length=150)),
                ('b', models.CharField(max_length=150)),
                ('c', models.CharField(max_length=150)),
                ('d', models.CharField(max_length=150)),
                ('true_answer', models.CharField(help_text='E.x: a', max_length=150)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.test')),
            ],
        ),
    ]

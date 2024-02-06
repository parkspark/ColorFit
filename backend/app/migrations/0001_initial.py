# Generated by Django 4.0.2 on 2022-03-11 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import hashid_field.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=100, unique=True)),
                ('nickname', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fashion',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False)),
                ('color', models.CharField(choices=[('SP', 'spring'), ('SU', 'summer'), ('AU', 'autumn'), ('WI', 'winter')], default='SP', max_length=2)),
                ('image', models.ImageField(upload_to='fashion/')),
                ('date', models.DateField()),
                ('spring_rate', models.IntegerField()),
                ('summer_rate', models.IntegerField()),
                ('autumn_rate', models.IntegerField()),
                ('winter_rate', models.IntegerField()),
                ('result', models.CharField(choices=[('G', 'good'), ('S', 'soso'), ('B', 'bad')], default='G', max_length=1)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='face/')),
                ('date', models.DateField()),
                ('spring_rate', models.IntegerField()),
                ('summer_rate', models.IntegerField()),
                ('autumn_rate', models.IntegerField()),
                ('winter_rate', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

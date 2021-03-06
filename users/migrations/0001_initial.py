# Generated by Django 4.0.4 on 2022-05-28 05:22

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kakao_id', models.CharField(max_length=50, unique=True)),
                ('area', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_item', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=50)),
                ('have_item', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=50)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user')),
            ],
            options={
                'db_table': 'users_item',
            },
        ),
    ]

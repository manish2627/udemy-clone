# Generated by Django 4.1 on 2022-08-06 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=16)),
                ('phone', models.CharField(max_length=15)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('mail_validate', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]

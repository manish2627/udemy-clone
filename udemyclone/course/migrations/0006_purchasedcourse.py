# Generated by Django 4.1 on 2022-08-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasedcourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.IntegerField()),
                ('purchase_id', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1 on 2022-08-08 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_purchasecourse_purchase_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasecourse',
            name='purchase_course',
        ),
    ]

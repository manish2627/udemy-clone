# Generated by Django 4.1 on 2022-08-08 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_remove_purchasecourse_purchase_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasecourse',
            name='purchase_course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1 on 2022-08-06 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_courselesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('video_name', models.CharField(max_length=20)),
                ('video_link', models.CharField(max_length=100)),
                ('video_desc', models.TextField(default='')),
                ('video_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('video_lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.courselesson')),
            ],
        ),
    ]

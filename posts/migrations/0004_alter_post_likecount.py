# Generated by Django 3.2.9 on 2021-12-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_likecount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likecount',
            field=models.IntegerField(blank=True, default=0, verbose_name='like_count'),
        ),
    ]

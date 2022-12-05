# Generated by Django 3.2.13 on 2022-12-05 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0008_merge_20221205_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='card_in_out',
        ),
        migrations.AlterField(
            model_name='detailcomment',
            name='rate',
            field=models.CharField(choices=[('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')], max_length=10),
        ),
    ]

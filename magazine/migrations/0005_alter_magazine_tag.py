# Generated by Django 3.2.13 on 2022-12-27 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_auto_20221226_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='tag',
            field=models.CharField(choices=[('ECT', '기타'), ('NEWS', '뉴스'), ('YEAR', '연말정산'), ('RECOMMEND', '추천·리뷰'), ('BASIC', '기초상식'), ('BODO', '보도자료')], default='ECT', max_length=20, verbose_name='태그명'),
        ),
    ]

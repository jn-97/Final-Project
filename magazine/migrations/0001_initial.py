# Generated by Django 3.2.13 on 2022-12-14 02:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='image/mzimg')),
                ('bookmark_users', models.ManyToManyField(related_name='bookmark_articles', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('grade', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine.magazine')),
                ('parent_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recomment', to='magazine.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

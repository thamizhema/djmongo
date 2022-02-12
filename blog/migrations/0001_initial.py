# Generated by Django 2.2 on 2022-02-09 09:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=20)),
                ('content', models.TextField(default='test')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
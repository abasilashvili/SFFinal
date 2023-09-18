# Generated by Django 4.2.2 on 2023-08-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletinboard', '0005_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimeCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_time_code', models.CharField(max_length=10, unique=True, verbose_name='Одноразовый код подтверждения')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
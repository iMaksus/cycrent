# Generated by Django 4.0.4 on 2022-05-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bicycle_user_delete_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=100)),
                ('date_birthday', models.DateTimeField(auto_now=True)),
                ('gender', models.CharField(max_length=10)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=40)),
                ('card_num', models.IntegerField()),
                ('card_date', models.DateTimeField(auto_now=True)),
                ('card_ccv', models.IntegerField()),
                ('profile_photo', models.ImageField(default='images/profiles/avatar.png', upload_to='images/%Y/%m/%d/')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

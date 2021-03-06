# Generated by Django 2.2.4 on 2020-04-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitYourTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=122)),
                ('last_name', models.CharField(max_length=122)),
                ('address1', models.CharField(max_length=230)),
                ('phone', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='tasks')),
            ],
        ),
    ]

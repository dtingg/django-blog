# Generated by Django 3.0.1 on 2019-12-31 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=128)),
                ('posts', models.ManyToManyField(blank=True, related_name='categories', to='blogging.Post')),
            ],
        ),
    ]
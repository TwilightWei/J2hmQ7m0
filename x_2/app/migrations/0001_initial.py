# Generated by Django 3.0.5 on 2020-04-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_number', models.IntegerField()),
                ('crwal_time', models.DateTimeField()),
            ],
        ),
    ]
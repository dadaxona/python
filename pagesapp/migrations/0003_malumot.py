# Generated by Django 3.2.9 on 2021-11-30 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagesapp', '0002_auto_20211130_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Malumot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('praduct', models.CharField(max_length=200)),
                ('soni', models.IntegerField()),
                ('narx', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 2.1.3 on 2018-11-10 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('description_text', models.TextField()),
                ('price_num', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

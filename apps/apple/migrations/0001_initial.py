# Generated by Django 4.2.11 on 2024-04-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppleCapacity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('province', models.CharField(max_length=50, unique=True, verbose_name='省份')),
                ('capacity', models.IntegerField(verbose_name='库容')),
            ],
            options={
                'verbose_name': '苹果库容',
                'verbose_name_plural': '苹果库容',
                'db_table': 'tb_apple_capacity',
            },
        ),
        migrations.CreateModel(
            name='AppleConsumption',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50, unique=True, verbose_name='国家')),
                ('consumption', models.IntegerField(verbose_name='消费量')),
            ],
            options={
                'verbose_name': '苹果消费',
                'verbose_name_plural': '苹果消费',
                'db_table': 'tb_apple_consumption',
            },
        ),
        migrations.CreateModel(
            name='AppleProduction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(verbose_name='年份')),
                ('production', models.IntegerField(verbose_name='产量')),
                ('global_production', models.IntegerField(verbose_name='全球产量')),
            ],
            options={
                'verbose_name': '苹果产量',
                'verbose_name_plural': '苹果产量',
                'db_table': 'tb_apple_production',
            },
        ),
        migrations.CreateModel(
            name='FruitPrice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=50, verbose_name='时间')),
                ('fruit', models.CharField(max_length=50, verbose_name='水果')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='价格')),
            ],
            options={
                'verbose_name': '水果价格',
                'verbose_name_plural': '水果价格',
                'db_table': 'tb_fruit_price',
            },
        ),
    ]

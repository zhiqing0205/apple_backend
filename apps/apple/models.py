from django.db import models


# Create your models here.

class AppleCapacity(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=50, verbose_name='省份', unique=True)
    capacity = models.IntegerField(verbose_name='库容')

    class Meta:
        db_table = 'tb_apple_capacity'
        verbose_name = '苹果库容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.province}：{self.capacity}吨'

    def to_dict(self):
        return {
            'province': self.province,
            'capacity': self.capacity
        }


class AppleConsumption(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, verbose_name='国家', unique=True)
    consumption = models.IntegerField(verbose_name='消费量')

    class Meta:
        db_table = 'tb_apple_consumption'
        verbose_name = '苹果消费'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.country}：{self.consumption}吨'

    def to_dict(self):
        return {
            'country': self.country,
            'consumption': self.consumption
        }


class AppleProduction(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='年份')
    production = models.IntegerField(verbose_name='产量')
    global_production = models.IntegerField(verbose_name='全球产量')

    class Meta:
        db_table = 'tb_apple_production'
        verbose_name = '苹果产量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.year}年：{self.production}吨'

    def to_dict(self):
        return {
            'year': self.year,
            'production': self.production,
            'global_production': self.global_production,
            'ratio': round(self.production / self.global_production, 2)
        }


class FruitPrice(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=50, verbose_name='时间')
    fruit = models.CharField(max_length=50, verbose_name='水果')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='价格')

    class Meta:
        db_table = 'tb_fruit_price'
        verbose_name = '水果价格'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.time}：{self.fruit}：{self.price}元/斤'

    def to_dict(self):
        return {
            'time': self.time,
            'fruit': self.fruit,
            'price': self.price
        }

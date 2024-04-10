import requests
from django.http import JsonResponse
import chardet

from apps.apple.models import AppleCapacity, AppleConsumption, AppleProduction, FruitPrice, AppleEfficiency


def crawl_apple_production_data():
    url = 'http://daping.agdata.cn/Api4Datas/appleList'
    response = requests.get(url)
    response.encoding = 'utf-8'
    apple_production_data = response.json()
    AppleProduction.objects.all().delete()
    for year, production, global_production in zip(apple_production_data[0][1:], apple_production_data[1][1:],
                                                   apple_production_data[2][1:]):
        try:
            AppleProduction.objects.create(year=year, production=production, global_production=global_production)
        except Exception as e:
            print(e)


def crawl_fruit_price_data():
    url = 'http://daping.agdata.cn/Api4Datas/fruitPrice'
    response = requests.get(url)
    response.encoding = 'utf-8'
    fruit_price_data = response.json()
    FruitPrice.objects.all().delete()

    fruit_price_instances = []

    for i in range(1, len(fruit_price_data)):
        fruit = fruit_price_data[i][0]
        for j, price in enumerate(fruit_price_data[i][1:]):
            time = fruit_price_data[0][j + 1]
            fruit_price_instances.append(FruitPrice(time=time, fruit=fruit, price=price))

    try:
        FruitPrice.objects.bulk_create(fruit_price_instances)
    except Exception as e:
        print(e)


def crawl_apple_capacity_data():
    url = 'http://daping.agdata.cn/Api4Datas/getDatas/7'
    response = requests.get(url)
    response.encoding = 'utf-8'
    apple_capacity_data = response.json()
    AppleCapacity.objects.all().delete()
    for province, capacity in zip(apple_capacity_data["14"][0][1:], apple_capacity_data["14"][1][1:]):
        try:
            AppleCapacity.objects.create(province=province, capacity=capacity)
        except Exception as e:
            print(e)


def crawl_apple_consumption_data():
    url = 'http://daping.agdata.cn/Api4Datas/getDatas/7'
    response = requests.get(url)
    response.encoding = 'utf-8'
    apple_consumption_data = response.json()
    AppleConsumption.objects.all().delete()
    for country, consumption in zip(apple_consumption_data["6"][0][1:], apple_consumption_data["6"][1][1:]):
        try:
            AppleConsumption.objects.create(country=country, consumption=consumption)
        except Exception as e:
            print(e)


def crawl_apple_efficiency_data():
    url = 'http://daping.agdata.cn/Api4Datas/getDatas/7'
    response = requests.get(url)
    response.encoding = 'utf-8'
    apple_efficiency_data = response.json()
    AppleEfficiency.objects.all().delete()
    for country, efficiency in zip(apple_efficiency_data["5"][0][1:], apple_efficiency_data["5"][1][1:]):
        try:
            AppleEfficiency.objects.create(country=country, efficiency=efficiency)
        except Exception as e:
            print(e)


def crawl_data(request):
    crawl_apple_production_data()
    crawl_fruit_price_data()
    crawl_apple_capacity_data()
    crawl_apple_consumption_data()
    crawl_apple_efficiency_data()

    return JsonResponse({'message': '数据爬取成功'})


def get_data(request):
    apple_production = [apple_production.to_dict() for apple_production in AppleProduction.objects.all()]
    apple_capacity = [apple_capacity.to_dict() for apple_capacity in AppleCapacity.objects.all()]
    apple_consumption = [apple_consumption.to_dict() for apple_consumption in AppleConsumption.objects.all()]
    fruit_price = FruitPrice.objects.all()
    times = set([price.time for price in fruit_price])
    fruits = set([price.fruit for price in fruit_price])
    apple_efficiency = [apple_efficiency.to_dict() for apple_efficiency in AppleEfficiency.objects.all()]

    return JsonResponse({
        'apple_production': {
            'years': [production['year'] for production in apple_production],
            'productions': [production['production'] for production in apple_production],
            'global_productions': [production['global_production'] for production in apple_production],
            'ratios': [production['ratio'] for production in apple_production]
        },
        'apple_capacity': apple_capacity,
        'apple_consumption': apple_consumption,
        'fruit_price': {
            'times': list(times),
            'fruits': [
                {
                    'label': fruit,
                    'data': [float(price.price) for price in fruit_price if price.fruit == fruit]
                }
                for fruit in fruits
            ]
        },
        'apple_efficiency': apple_efficiency
    })
import requests
from django.http import JsonResponse
import chardet
from apps.apple.models import AppleCapacity, AppleConsumption, AppleProduction, FruitPrice


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
            time = fruit_price_data[0][j]
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
        province = province.encode('utf-8').decode('utf-8')
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


def crawl_data(request):
    crawl_apple_production_data()
    crawl_fruit_price_data()
    crawl_apple_capacity_data()
    crawl_apple_consumption_data()

    return JsonResponse({'message': '数据爬取成功'})
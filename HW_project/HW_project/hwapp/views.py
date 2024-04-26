from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse
import logging
from django.shortcuts import  render
from .models import Client, Order, Product

logger = logging.getLogger(__name__)
def index(request):
    return HttpResponse("<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. <br>Dolores ea itaque laboriosam neque nihil odio provident quis quo tempore vitae.</p>")


def about(request):
    context = {'new': 'new'}
    return render(request, 'hwapp/about.html', context)


def get_clients(request):
    clients = Client.objects.all()
    return HttpResponse(clients)

def get_client(request):
    id = request.GET.get('id')
    client = Client.objects.get(id=int(id))
    return HttpResponse(client)

def get_order_info(request):
    client_id = request.GET.get('id')
    if client_id:
        order = Order.objects.get(client_id=int(client_id))
        return HttpResponse(order)
    else:
        all_orders = {}
        orders = Order.objects.all()
        for order in orders:
            all_orders[order.client_id] = int(order.total_cost)
        return HttpResponse(f'{all_orders}')


"""
Продолжаем работать с товарами и заказами.
Создайте шаблон, который выводит список заказанных
клиентом товаров из всех его заказов с сортировкой по
времени:
○ за последние 7 дней (неделю)
○ за последние 30 дней (месяц)
○ за последние 365 дней (год)

"""

def get_orders(request, client_id, period):
    client = Client.objects.get(id=int(client_id))
    if period == 'week':
        print(datetime.now()-timedelta(days=7))
        products = Product.objects.filter(order__client_id = client_id,order__date_ordered__gte=datetime.now()-timedelta(days=7))
        return render(request, 'hwapp/client_order.html', {'products': products, 'client': client})
    elif period == 'month':
        products = Product.objects.filter(order__client_id = client_id,order__date_ordered__gte=datetime.now()-timedelta(days=30))
        return render(request, 'hwapp/client_order.html', {'products': products, 'client': client})
    elif period == 'year':
        products = Product.objects.filter(order__client_id = client_id,order__date_ordered__gte=datetime.now()-timedelta(days=365))
        return render(request, 'hwapp/client_order.html', {'products': products, 'client': client})
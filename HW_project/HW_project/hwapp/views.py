from django.shortcuts import render
from django.http import HttpResponse
import logging

from .models import Client, Order
logger = logging.getLogger(__name__)
def index(request):
    return HttpResponse("<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. <br>Dolores ea itaque laboriosam neque nihil odio provident quis quo tempore vitae.</p>")


def about(request):
    return HttpResponse("about")


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

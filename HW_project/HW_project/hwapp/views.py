from datetime import datetime, timedelta

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
import logging
from django.shortcuts import render
from .models import Client, Order, Product
from .forms import ProductForm, ImageForm, ChoiceForm

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse(
        "<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. <br>Dolores ea itaque laboriosam neque nihil odio provident quis quo tempore vitae.</p>")


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
        print(datetime.now() - timedelta(days=7))
        products = Product.objects.filter(order__client_id=client_id,
                                          order__date_ordered__gte=datetime.now() - timedelta(days=7))
        return render(request, 'hwapp/client_order.html', {'products': products, 'client': client})
    elif period == 'month':
        products = Product.objects.filter(order__client_id=client_id,
                                          order__date_ordered__gte=datetime.now() - timedelta(days=30))
        return render(request, 'hwapp/client_order.html', {'products': products, 'client': client})
    elif period == 'year':
        products = Product.objects.filter(order__client_id=client_id,
                                          order__date_ordered__gte=datetime.now() - timedelta(days=365))
        return render(request, 'hwapp/client_order.html', {'products': products, 'client': client})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product(product_name=form.cleaned_data['product_name'],
                              description=form.cleaned_data['description'],
                              price=form.cleaned_data['price'],
                              quantity=form.cleaned_data['quantity'],
                              added_date=form.cleaned_data['added_date'],
                              )
            product.save()
            return HttpResponse('Товар создан')
    else:

        form = ProductForm()
    return render(request, 'hwapp/forms_render.html', {'form': form})


def upload_image(request, product_id):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():

            product = Product.objects.get(id = product_id)
            product.link_photo = request.FILES['image']
            product.save()
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'hwapp/upload_image.html', {'form': form})


def update_product(request, product_id):
    if request.method == 'POST':
        form = ChoiceForm(request.POST, instance=Product.objects.get(id=product_id))
        form.save()
        return HttpResponse('Данные обновлены')
    else:
        product = Product.objects.get(id=product_id)
        form = ChoiceForm(
            instance=product
        )
    return render(request, 'hwapp/upload_image.html', {'form': form})

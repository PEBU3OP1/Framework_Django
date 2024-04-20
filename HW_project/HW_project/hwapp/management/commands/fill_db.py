from django.core.management.base import BaseCommand
from datetime import date
from hwapp.models import Client, Product, Order



class Command(BaseCommand):
    help = 'Update client name'
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='id of client')

    def handle(self, *args, **kwargs):
       count = kwargs['count']
       for prod in range(1, count + 1):
           product = Product(product_name = f'prod{prod}', price = prod * 100, quantity = prod)
           product.save()
       for i in range(1, count + 1):
           client = Client(name=f'Saveliy{i}', email=f'a@{i}mail.ru', phone = f'890320546{i}', address = 'fdsfsdd fds', registered_date = date.today())
           client.save()
       for j in range(1, 4):
           order = Order(
               client = Client.objects.filter(id=21 + j).first(),
               # products = [Product.objects.filter(id=1).first(),Product.objects.filter(id=2).first()]
               total_cost = 0

           )
           order.save()

from django.core.management.base import BaseCommand
from datetime import date
from hwapp.models import Order, Product, Client



class Command(BaseCommand):
    help = 'Update client name'


    def handle(self, *args, **kwargs):

       order = Order()
       order.client_id = 2
       order.total_cost = 2000

       order.save()


       order.products.add(Product.objects.get(id = 1))
       order.products.add(Product.objects.get(id=2))



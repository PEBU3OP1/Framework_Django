from django.core.management.base import BaseCommand
from datetime import date
from hwapp.models import Product



class Command(BaseCommand):
    help = 'Update client name'


    def handle(self, *args, **kwargs):

       product = Product(product_name='Smetana', description='sourcream', price=10, quantity=3)
       product.save()
       product = Product(product_name='Moloko', description='Milk', price=8, quantity=7,
                       added_date='2022-05-21')
       product.save()
       product = Product(product_name='Kefir', description='Ryajhenka', price=15, quantity=11,
                       added_date='2021-05-21')
       product.save()


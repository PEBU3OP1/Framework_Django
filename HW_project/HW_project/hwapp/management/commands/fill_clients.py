from django.core.management.base import BaseCommand
from datetime import date
from hwapp.models import Client



class Command(BaseCommand):
    help = 'Update client name'
    # def add_arguments(self, parser):
    #     parser.add_argument('count', type=int, help='id of client')

    def handle(self, *args, **kwargs):

       client = Client(name=f'Vsevolod', email=f'Vsevolod@mail.ru', phone = f'890320546', address = 'fdsfsdd fds', registered_date = date.today())
       client.save()
       client = Client(name=f'Dima', email=f'Dima@mail.ru', phone=f'899999999', address='fdsfsdd fds',
                       registered_date='2023-05-21')
       client.save()
       client = Client(name=f'Misha', email=f'Misha@mail.ru', phone=f'888888888', address='fdsfsdd fds',
                       registered_date='2024-04-14')
       client.save()


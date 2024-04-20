from django.core.management.base import BaseCommand
from datetime import date
from hwapp.models import Client


class Command(BaseCommand):
    help = 'Create clinet in DB'
    def handle(self, *args, **kwargs):
        client = Client(name='seva', email='a@mail.ru', phone = '8903205468', address = 'fdsfsdd fds', registered_date = date.today())
        client.save()
        self.stdout.write(self.style.SUCCESS('Successfully created'))
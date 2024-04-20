from django.core.management.base import BaseCommand
from datetime import date
from hwapp.models import Client


class Command(BaseCommand):
    help = 'Get client by id'
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of client')
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(self.style.SUCCESS(f'{client}'))
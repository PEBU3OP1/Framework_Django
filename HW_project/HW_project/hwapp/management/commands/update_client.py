from django.core.management.base import BaseCommand
from datetime import date
from hwapp.models import Client


class Command(BaseCommand):
    help = 'Update client name'
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of client')
        parser.add_argument('name', type=str, help='client name')
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        name = kwargs['name']
        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.save()
        self.stdout.write(self.style.SUCCESS(f'{client}'))
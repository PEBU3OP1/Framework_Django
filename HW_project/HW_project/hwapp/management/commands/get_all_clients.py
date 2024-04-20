from django.core.management.base import BaseCommand
from datetime import date
from hwapp.models import Client


class Command(BaseCommand):
    help = 'Get all clients from database'
    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        self.stdout.write(self.style.SUCCESS(f'{clients}'))
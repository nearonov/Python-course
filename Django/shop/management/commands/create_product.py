from shop.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Created product")

        products = [
            'Printer', 'Noutboock', 'Iphon'

        ]
        for product in products:
            category, created = Product.objects.get_or_create(name=product)
            self.stdout.write(f'Created products {category.name}')

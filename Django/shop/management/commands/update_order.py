from django.core.management.base import BaseCommand
from shop.models import Product, Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Update order")
        order = Order.objects.first()                #filter(user_id=2)
        if not order:
            self.stdout.write("Немає заказа.")
            return
        products = Product.objects.filter(name='Printer')
        for product in products:
            order.products.add(product)
        order.save()

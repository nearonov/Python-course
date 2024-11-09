from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from shop.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Creat order")
        user = User.objects.get(username='ivanhoe')
        order = Order.objects.get_or_create(delivery_address="Rivne st.Vidinska,25 apart 50",
                                            promo_code='6e3E5GH', user=user
                                            )
        self.stdout.write(f"Creat order  {order} ")


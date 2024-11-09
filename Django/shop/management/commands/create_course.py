from django.core.management.base import BaseCommand
from shop.models import  Course
from django.utils import timezone


class Command(BaseCommand):
    """ Created course """
    def handle(self, *args, **kwargs):
        element = Course.objects.get_or_create(title='Photoshop', price=120, category_id=2)
        self.stdout.write(f"Created course {element}")

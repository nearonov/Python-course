from django.core.management.base import BaseCommand
from shop.models import Category
from django.utils import timezone

class Command(BaseCommand):
    """ Created category """

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Creat category"))

        category_title = [
            'web designer',
            'DataSense'
        ]
        for title in category_title:
            category, created = Category.objects.get_or_create(title=title)
            self.stdout.write(f"Created category {category.title}")

        self.stdout.write(self.style.SUCCESS('Category created'))

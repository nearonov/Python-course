from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=255)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(blank=True, null=True)
    students_qty = models.IntegerField(blank=True, null=True)
    reviews_qty = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    foto = models.ImageField(upload_to='images',
                             help_text="Введіть зображення курсів",
                             verbose_name="Зображення курсів",
                             blank=True)

    # Курси розтошувати в алфавитном порядку
    class Meta:
        ordering = ['title']
        verbose_name = 'Назва курсів'

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    delivery_address = models.TextField(null=False, blank=True)
    promo_code = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')

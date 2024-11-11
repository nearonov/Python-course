from django.contrib import admin
from . import models
from shop.models import Category, Course,Product,Order

admin.site.register(models.Course)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Order)
# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'students_qty', 'reviews_qty', ' create_at')

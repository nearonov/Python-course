from django.contrib import admin
from . import models
from shop.models import Category, Course, Product, Order
from django.utils.html import format_html

# admin.site.register(models.Course)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Order)


# @admin.register(Course)

class CourseAdmin(admin.ModelAdmin):  # Изменение конфигурации административной панели
    list_display = ('title', 'show_photo', 'create_at', 'price', 'students_qty',
                    'reviews_qty', 'foto')
    list_filter = ('category',)  # фільтр по категоріям
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        try:
            return format_html(f'<img src="{obj.foto.url}" style ="max-height: 70px;">')

        except:
            pass  # just ignore

    show_photo.short_description = 'Обложка'


admin.site.register(Course, CourseAdmin)

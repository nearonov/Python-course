from shop.models import Course, Product
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'category', 'price',
                  'students_qty', 'reviews_qty']

from django.urls import path, re_path
from shop.views import *

app_name = 'shop'
urlpatterns = [
    path('', index, name='index'),
    #re_path(r'^about', about, name='about'),  # url для def
    path('about/', CourseCreate.as_view(), name='about'),
    re_path(r'product/(?P<id_producte>\d+)/(?P<producte>\D+)/', product),
    path('groups/', groups_list, name='groups-list'),
    path('products/', products_list, name='products-list'),
    path('order/', order_list, name='order-list'),
    path('<int:id>', single_course, name='single'),
    path('other-form/', other_form, name='other-form'),
    # path('<int:id>//', delete, name='delete'), # url для def
    path('<int:pk>//', CourseDelete.as_view(), name='delete'),
    # path('<int:id>/', edit, name=' edit'), # url для def
    path('<int:pk>/', CourseUpdate.as_view(), name=' edit'),  # url для class

]

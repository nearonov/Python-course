from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest  # для анатаціі типів request
from django.contrib.auth.models import Group
from .models import Course, Product,Order
from .forms import CourseForm


def index(request: HttpRequest):
    courses = Course.objects.all()
    return render(request, "shop/courses.html", {'courses': courses})


def about(request: HttpRequest):
    if request.method == 'POST':
        my_form = CourseForm(request.POST)
        if my_form.is_valid():
            my_form.save()
        return redirect('index')

    my_form = CourseForm()
    context = {'form': my_form}
    return render(request, 'shop/my_form.html', context)


def product(request, id_producte, producte):
    output = "<h2>Продукт:№{0}</h2> <h3>Імя продукта : {1}</h3>".format(id_producte, producte)
    return HttpResponse(output)


def groups_list(request: HttpRequest):
    groups = Group.objects.prefetch_related('permissions').all()
    cotext = {
        'groups': groups
    }
    return render(request, "shop/groups-list.html", cotext)


def products_list(request: HttpRequest):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "shop/products-list.html", context)

def order_list(request:HttpRequest):
    orders = Order.objects. select_related('user').prefetch_related('products').all()
    context ={
        'orders': orders
    }
    return render(request, "shop/order-list.html", context)


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404  # для анатаціі типів request
from django.contrib.auth.models import Group
from .models import Course, Product, Order
from .forms import CourseForm, CourseEdit
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
import requests


def index(request: HttpRequest):
    courses = Course.objects.all()
    return render(request, "shop/courses.html", {'courses': courses})


def other_form(request: HttpRequest):
    courses = Course.objects.all()
    return render(request, "shop/other_form.html", {'courses': courses})


# Ввід курсів при допомозі класа CreateView
class CourseCreate(CreateView):
    model = Course
    fields = ['title', 'category', 'price', 'students_qty', 'reviews_qty', 'foto']
    success_url = reverse_lazy("shop:index")


# Ввід курсів при допомозі функціі
# def about(request: HttpRequest):
#     if request.method == 'POST':
#         my_form = CourseForm(request.POST)
#         if my_form.is_valid():
#             my_form.save()
#         return redirect('shop:index')
#
#     my_form = CourseForm()
#     context = {'form': my_form}
#     return render(request, 'shop/my_form.html', context)


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


def order_list(request: HttpRequest):
    orders = Order.objects.select_related('user').prefetch_related('products').all()
    context = {
        'orders': orders
    }
    return render(request, "shop/order-list.html", context)


def single_course(request: HttpRequest, id):
    try:
        course = Course.objects.get(pk=id)
        return render(request, "shop/single_course.html", {"course": course})
    except Course.DoesNotExist:
        raise Http404()


def delete(request: HttpRequest, id):
    course = Course.objects.get(pk=id)
    course.delete()
    return redirect('shop:index')


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy("shop:index")


# def edit(request: HttpRequest, id):
#     course = Course.objects.get(id=id)
#     if request.method == 'POST':
#         course.title = request.POST.get('title')
#         # course.category = request.POST.get('category')
#         course.price = request.POST.get('price')
#         course.save()
#         return redirect('shop:index')
#
#     else:
#         courses = CourseEdit()
#         context = {'form': courses}
#         return render(request, 'shop/update_course.html', context)
#

# редогування на основі класа UpdateView
class CourseUpdate(UpdateView):
    model = Course
    fields = ['title', 'price', 'foto']
    success_url = reverse_lazy('shop:index')

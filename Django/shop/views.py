from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404  # для анатаціі типів request
from django.contrib.auth.models import Group
from .models import Course, Product, Order
from .forms import CourseForm, CourseEdit, ProductsCreate
from django.views import View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
import requests


# def index(request: HttpRequest):
#     courses = Course.objects.all()
#     return render(request, "shop/courses.html", {'courses': courses})


# class Index(TemplateView):
#     template_name = 'shop/courses.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['courses'] = Course.objects.all()
#         return context

class Index(ListView):
    template_name = 'shop/courses.html'
    model = Course
    context_object_name = 'courses'


def other_form(request: HttpRequest):
    courses = Course.objects.all()
    return render(request, "shop/other_form.html", {'courses': courses})


# Ввід курсів при допомозі класа CreateView
class CourseCreate(CreateView):
    model = Course
    fields = ['title', 'category', 'price', 'students_qty', 'reviews_qty', 'foto']
   # form_class = CourseForm
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
#     return render(request, 'shop/course_form.html', context)


def product(request, id_producte, producte):
    output = "<h2>Продукт:№{0}</h2> <h3>Імя продукта : {1}</h3>".format(id_producte, producte)
    return HttpResponse(output)


def groups_list(request: HttpRequest):
    groups = Group.objects.prefetch_related('permissions').all()
    cotext = {
        'groups': groups
    }
    return render(request, "shop/groups-list.html", cotext)


class ProductsList(View):
    def get(self, request: HttpRequest):
        products = Product.objects.all()
        form = ProductsCreate()
        context = {
            'products': products,
            'form': form
        }
        return render(request, "shop/products-list.html", context)

    def post(self, request: HttpRequest):
        form = ProductsCreate(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)


# class ProductDetailsView(View):
#     def get(self, request: HttpRequest, pk: int):
#         # product = Product.objects.get(pk=pk)
#         product = get_object_or_404(Product, pk=pk)
#         return render(request, "shop/product-details.html", {"product": product})
class ProductDetailsView(DetailView):
    template_name = 'shop/product-details.html'
    model = Product
    context_object_name = 'product'


# Відображення продуктів при допомозі функціі
# def products_list(request: HttpRequest):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, "shop/products-list.html", context)


# def order_list(request: HttpRequest):
#     orders = Order.objects.select_related('user').prefetch_related('products').all()
#     context = {
#         'orders': orders
#     }
#     return render(request, "shop/order-list.html", context)


class OrderList(ListView):
    template_name = 'shop/order-list.html'
    queryset = (
        Order.objects.select_related('user').prefetch_related('products')
    )
    context_object_name = 'orders'


# def single_course(request: HttpRequest, id):
#     try:
#         course = Course.objects.get(pk=id)
#         return render(request, "shop/single_course.html", {"course": course})
#     except Course.DoesNotExist:
#         raise Http404()


class SingleCourse(DetailView):
    template_name = 'shop/single_course.html'
    model = Course
    context_object_name = 'course'


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
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('shop:index')

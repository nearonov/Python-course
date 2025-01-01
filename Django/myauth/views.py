from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, forms
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from myauth.models import *

class RegisterVieww(CreateView):
    form_class = forms.UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy('myauth:about-me')

    # Аунтіфікація пользователя після регістраціі.
    def form_valid(self, form):
        response = super().form_valid(form)
        Account.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response


class AboutMeView(TemplateView):
    template_name = 'myauth/about-me.html'


def login_view(request: HttpRequest):
    if request.method == 'GET':
        # if request.user.is_authenticated:
        # return redirect('myauth:login')
        # return HttpResponse("<h2>Ви вже здіїснили вхід!</h2>")
        return render(request, 'myauth/login.html')
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('shop:index')
    return render(request, 'myauth/login.html', {'error': 'invalid login credentials'})


class BBLoginView(LoginView):
    template_name = 'myauth/login.html'
    redirect_authenticated_user = True


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'myauth/logout.html'
# next_page = reverse_lazy('shop:index')

from django.urls import path, re_path
from myauth.views import *

app_name = 'myauth'
urlpatterns = [
    #path('', login_view, name='login'),
    path('', BBLoginView.as_view(), name='login'),
    path('logout/', BBLogoutView.as_view(), name='logout'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('register/', RegisterVieww.as_view(), name='register'),
]

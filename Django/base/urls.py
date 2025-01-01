from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('shop/', include('shop.urls')),
    path('myauth/', include('myauth.urls')),
    path('myapiapp/', include('myapiapp.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

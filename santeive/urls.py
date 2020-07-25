from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Para la app core
    path('', include('core.urls')),
    #Para nuestro admin
    path('admin/', admin.site.urls),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

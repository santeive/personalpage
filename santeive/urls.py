from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Para la app core
    path('', include('core.urls')),
    #Para nuestro admin
    path('admin/', admin.site.urls),
<<<<<<< HEAD
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> e8d9c76831f33b92f7d0739a0c40cf4ef7ae374e

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Para la app core
    path('', include('core.urls')),
    #Para nuestro admin
    path('admin/', admin.site.urls),
]

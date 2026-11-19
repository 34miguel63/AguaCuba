from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Aquí se irán agregando las rutas de las apps, ej: path('', include('apps.search.urls')),
]
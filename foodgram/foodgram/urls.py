from django.contrib import admin
from django.urls import include, path
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

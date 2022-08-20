from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('users.urls', namespace='api_users')),
    path('api/', include('api.urls', namespace='api')),
    path('api/auth/token/login/', views.obtain_auth_token),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet

router = DefaultRouter()
router.register(r'recipes', PostViewSet, basename='recipes')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

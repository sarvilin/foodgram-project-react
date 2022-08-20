from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RecipeViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('', include(router.urls)),
]

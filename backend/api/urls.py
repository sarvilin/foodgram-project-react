from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RecipeViewSet, TagsViewSet, IngredientsViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'ingredients', IngredientsViewSet, basename='ingredients')
router.register(r'tags', TagsViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
]

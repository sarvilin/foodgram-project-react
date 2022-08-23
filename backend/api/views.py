from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        AllowAny)
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import (RecipeSerializer, TagSerializer,
                             IngredientSerializer)
from recipes.models import Recipe, Tag, Ingredient


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagsViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class IngredientsViewSet(ReadOnlyModelViewSet):
    # permission_classes = (IsAdminOrReadOnly,)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    # filter_backends = (IngredientSearchFilter,)
    search_fields = ('^name',)

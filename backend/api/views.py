from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        AllowAny)

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


# class IngredientsViewSet(viewsets.ModelViewSet):
#     serializer_class = IngredientSerializer
#     queryset = Ingredient.objects.all()
#     pagination_class = None
#     permission_classes = (AllowAny,)
#     # filterset_class = IngredientNameFilter
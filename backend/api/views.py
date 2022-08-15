from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)

from api.permissions import IsAuthorChangeDeleteOnly
from api.serializers import (RecipeSerializer)
from recipes.models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorChangeDeleteOnly]
    # pagination_class = LimitOffsetPagination
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

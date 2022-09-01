from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        AllowAny, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.filter import AuthorAndTagFilter, IngredientSearchFilter
from api.pagination import LimitPageNumberPagination
from api.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from api.serializers import (RecipeSerializer, TagSerializer,
                             IngredientSerializer, CropRecipeSerializer)
from recipes.models import (Recipe, Tag, Ingredient, Favorite, Cart,
                            RecipeIngredient)


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None


class IngredientsViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (IngredientSearchFilter,)
    search_fields = ('^name',)
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filter_class = AuthorAndTagFilter
    pagination_class = LimitPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        detail=True,
        methods=['get', 'delete'],
        permission_classes=[IsAuthenticated]
    )
    def favorite(self, request, pk=None):
        if request.method == 'GET':
            return self.add_obj(Favorite, request.user, pk)
        elif request.method == 'DELETE':
            return self.delete_obj(Favorite, request.user, pk)
        return None

    @action(
        detail=True,
        methods=['get', 'delete'],
        permission_classes=[IsAuthenticated]
    )
    def shopping_cart(self, request, pk=None):
        if request.method == 'GET':
            return self.add_obj(Cart, request.user, pk)
        elif request.method == 'DELETE':
            return self.delete_obj(Cart, request.user, pk)
        return None

    # @action(detail=False, methods=['get'],
    #         permission_classes=[IsAuthenticated])
    # def download_shopping_cart(self, request):
    #     final_list = {}
    #     ingredients = RecipeIngredient.objects.filter(
    #         recipe__cart__user=request.user).values_list(
    #         'ingredient__name', 'ingredient__measurement_unit',
    #         'amount')
    #     for item in ingredients:
    #         name = item[0]
    #         if name not in final_list:
    #             final_list[name] = {
    #                 'measurement_unit': item[1],
    #                 'amount': item[2]
    #             }
    #         else:
    #             final_list[name]['amount'] += item[2]
    #     pdfmetrics.registerFont(
    #         TTFont('Slimamif', 'Slimamif.ttf', 'UTF-8'))
    #     response = HttpResponse(content_type='application/pdf')
    #     response['Content-Disposition'] = ('attachment; '
    #                                        'filename="shopping_list.pdf"')
    #     page = canvas.Canvas(response)
    #     page.setFont('Slimamif', size=24)
    #     page.drawString(200, 800, 'Список ингредиентов')
    #     page.setFont('Slimamif', size=16)
    #     height = 750
    #     for i, (name, data) in enumerate(final_list.items(), 1):
    #         page.drawString(75, height, (f'<{i}> {name} - {data["amount"]}, '
    #                                      f'{data["measurement_unit"]}'))
    #         height -= 25
    #     page.showPage()
    #     page.save()
    #     return response

    def add_obj(self, model, user, pk):
        if model.objects.filter(user=user, recipe__id=pk).exists():
            return Response({
                'errors': 'Рецепт уже добавлен в список'
            }, status=status.HTTP_400_BAD_REQUEST)
        recipe = get_object_or_404(Recipe, id=pk)
        model.objects.create(user=user, recipe=recipe)
        serializer = CropRecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_obj(self, model, user, pk):
        obj = model.objects.filter(user=user, recipe__id=pk)
        if obj.exists():
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({
            'errors': 'Рецепт уже удален'
        }, status=status.HTTP_400_BAD_REQUEST)

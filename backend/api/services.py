from datetime import datetime as dt
from string import hexdigits

from django.db.models import F, Sum
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST

from recipes.models import RecipeIngredient

DATE_TIME_FORMAT = '%d/%m/%Y %H:%M'

incorrect_layout = str.maketrans(
    'qwertyuiop[]asdfghjkl;\'zxcvbnm,./',
    'йцукенгшщзхъфывапролджэячсмитьбю.'
)


def recipe_amount_ingredients_set(recipe, ingredients):
    for ingredient in ingredients:
        RecipeIngredient.objects.get_or_create(
            recipe=recipe,
            ingredients=ingredient['ingredient'],
            amount=ingredient['amount']
        )


def check_value_validate(value, klass=None):
    if not str(value).isdecimal():
        raise ValidationError(f'{value} должно содержать цифру')
    if klass:
        obj = klass.objects.filter(id=value)
        if not obj:
            raise ValidationError(f'{value} не существует')
        return obj[0]


def is_hex_color(value):
    if len(value) not in (3, 6):
        raise ValidationError(f'{value} неправильной длины ({len(value)}).')
    if not set(value).issubset(hexdigits):
        raise ValidationError(f'{value} нешестнадцатиричное')


def generate_shopping_list(user):
    if not user.carts.exists():
        return Response(status=HTTP_400_BAD_REQUEST)
    ingredients = RecipeIngredient.objects.filter(
        recipe__in=(user.carts.values('id'))).values(
        ingredient=F('ingredients__name'),
        measure=F('ingredients__measurement_unit')
    ).annotate(amount=Sum('amount'))

    time_now = dt.now().strftime(DATE_TIME_FORMAT)
    shopping_list = (
        f'Список покупок для:\n\n{user.first_name}\n\n'
        f'{time_now}\n\n'
    )
    shopping_list += '\n'.join([
        f'{ingredient["ingredient"]} - {ingredient["amount"]} '
        f'{ingredient["measure"]}'
        for ingredient in ingredients
    ])
    shopping_list += '\n\nВыгрузка из Foodgram'
    return shopping_list



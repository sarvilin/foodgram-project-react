from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db.models import (
    CASCADE, CharField, DateTimeField, ForeignKey, ImageField,
    ManyToManyField, Model, PositiveSmallIntegerField, TextField,
    UniqueConstraint
)
from django.db.models.functions import Length

CharField.register_lookup(Length)

User = get_user_model()


class Tag(Model):
    name = CharField(
        verbose_name='Название',
        max_length=200,
        unique=True,
    )
    color = ColorField(
        verbose_name='Цветовой HEX-код',
        format='hex',
        unique=True,
        default='#FF0000',
    )
    slug = CharField(
        verbose_name='Slug',
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name', )

    def __str__(self):
        return self.name


class Ingredient(Model):
    name = CharField(
        verbose_name='Название ингредиента',
        max_length=200,
    )
    measurement_unit = CharField(
        verbose_name='Единица измерения',
        max_length=200,
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name', )

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Recipe(Model):
    name = CharField(
        verbose_name='Название рецепта',
        max_length=200,
    )
    author = ForeignKey(
        verbose_name='Автор публикации',
        related_name='recipes',
        to=User,
        on_delete=CASCADE,
    )
    favorite = ManyToManyField(
        verbose_name='Понравившиеся рецепты',
        related_name='favorites',
        to=User,
    )
    tags = ManyToManyField(
        verbose_name='Теги',
        related_name='recipes',
        to=Tag,
    )
    ingredients = ManyToManyField(
        verbose_name='Ингредиенты',
        related_name='recipes',
        to=Ingredient,
        through='recipes.RecipeIngredient',
    )
    cart = ManyToManyField(
        verbose_name='Список покупок',
        related_name='carts',
        to=User,
    )
    pub_date = DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    image = ImageField(
        verbose_name='Картинка',
        upload_to='recipes/',
    )
    text = TextField(
        verbose_name='Текстовое описание',
        max_length=200,
    )
    cooking_time = PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        validators=(MinValueValidator(
            1, message='Минимальное время приготовления 1 минута'),),
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date', )
        constraints = (
            UniqueConstraint(
                fields=('name', 'author'),
                name='unique_for_author'
            ),
        )

    def __str__(self):
        return self.name


class RecipeIngredient(Model):
    recipe = ForeignKey(
        verbose_name='В рецептах',
        related_name='ingredient',
        to=Recipe,
        on_delete=CASCADE,
    )
    ingredients = ForeignKey(
        verbose_name='Связанные ингредиенты',
        related_name='recipe',
        to=Ingredient,
        on_delete=CASCADE,
    )
    amount = PositiveSmallIntegerField(
        verbose_name='Количество ингредиента',
        default=0,
        validators=[MinValueValidator(1)],
    )

    class Meta:
        verbose_name = 'Количество ингридиента'
        verbose_name_plural = 'Количество ингридиентов'
        ordering = ['recipe']

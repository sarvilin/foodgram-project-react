from django.contrib import admin

from recipes.models import (Tag, Ingredient, Recipe,
                            RecipeIngredient, Favorite, ShoppingCart)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    list_filter = ('name',)
    search_fields = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'count_favorites')
    list_filter = ('author', 'name', 'tags')

    def count_favorites(self, obj):
        return obj.favorites.count()


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)



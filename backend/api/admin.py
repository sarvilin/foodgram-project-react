from django.contrib import admin

from recipes.models import (Tag, Ingredient, Recipe,
                            RecipeIngredient, Favorite, Cart)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    list_filter = ('name',)
    search_fields = ('name',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)


class AmountIngredients(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    # min_num = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'count_favorites')
    search_fields = ('name', 'author')
    list_filter = ('author', 'name', 'tags')
    filter_horizontal = ('ingredients',)
    inlines = [AmountIngredients, ]

    def count_favorites(self, obj):
        return obj.favorites.count()

    count_favorites.short_description = 'В избранном'


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Favorite)
admin.site.register(Cart)



from django.contrib import admin

from recipes.models import Tag, Ingredient, Recipe


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')


# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'author', 'count_favorites')
#     list_filter = ('author', 'name', 'tags')
#
#     def count_favorites(self, obj):
#         return obj.favorites.count()



# class IngredientAdmin(admin.ModelAdmin):
#     list_display = ('name', 'measurement_unit')
#     search_fields = ('^name',)


# admin.site.register(IngredientAdmin)
admin.site.register(Tag, TagAdmin)
# admin.site.register(Recipe, RecipeAdmin)

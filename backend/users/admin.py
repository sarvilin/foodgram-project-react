from django.contrib import admin

from users.models import Follow, User


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name', 'measurement_unit')
#     list_filter = ('name',)
#     search_fields = ('name',)


admin.site.register(Follow)
# admin.site.register(UserAdmin)


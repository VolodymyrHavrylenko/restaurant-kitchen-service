from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from kitchen.models import (
    Cook,
    Dish,
    DishType,
    Ingredient
)

admin.site.unregister(Group)
@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "year_of_experience",
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {"fields": ("year_of_experience",)}
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                "first_name",
                "last_name",
                "year_of_experience",
            )
            }
        ),
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display =["name", "dish_type", "price", "description"]
    list_filter = ["dish_type", "ingredient"]
    search_fields = ["name", "cook__username"]

admin.site.register(DishType)
admin.site.register(Ingredient)




from django.urls import path

from kitchen.models import Ingredient
from kitchen.views import (
    index,
    CookListView,
    DishListView,
    DishTypeListView,
    IngredientListView,
    CookDetailView,
    DishDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dished/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish_types", DishTypeListView.as_view(), name="dish-type-list"),
    path("ingredients", IngredientListView.as_view(), name="ingredient-list"),

]

app_name = "kitchen"

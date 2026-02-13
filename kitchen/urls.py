from django.urls import path

from kitchen.models import Ingredient
from kitchen.views import (
    index,
    CookListView,
    DishListView,
    DishTypeListView,
    IngredientListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks"),
    path("dishes/", DishListView.as_view(), name="dishes"),
    path("dish_types", DishTypeListView.as_view(), name="dish-types"),
    path("ingredients", IngredientListView.as_view(), name="ingredients"),

]

app_name = "kitchen"
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
    CookCreateView,
    DishCreateView,
    DishTypeCreateView,
    IngredientCreateView,
    CookUpdateView,
    DishUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dished/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update", DishUpdateView.as_view(), name="dish-update"),
    path("dish_types", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("ingredients", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create", IngredientCreateView.as_view(), name="ingredient-create"),

]

app_name = "kitchen"

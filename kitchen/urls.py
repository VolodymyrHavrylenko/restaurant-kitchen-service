from django.urls import path

from kitchen.views import (
    index,
    CookListView,
    DishListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookListView.as_view(), name="cooks"),
    path("dishes/", DishListView.as_view(), name="dishes"),
]

app_name = "kitchen"
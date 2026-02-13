from django.views import generic
from django.shortcuts import render

from kitchen.models import Cook, Dish, DishType, Ingredient


def index(request):
    cooks = Cook.objects.count()
    dishes = Dish.objects.count()
    types_of_dishes = DishType.objects.count()
    ingredients = Ingredient.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "cooks": cooks,
        "dishes": dishes,
        "types_of_dishes": types_of_dishes,
        "ingredients": ingredients,
        "num_visits": request.session["num_visits"],
    }
    return render(request, "kitchen/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 10

    def get_queryset(self):
        return Dish.objects.select_related("dish_type").prefetch_related(
            "ingredient",
            "cook"
        )


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 4
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class IngredientListView(generic.ListView):
    model = Ingredient
    paginate_by = 5

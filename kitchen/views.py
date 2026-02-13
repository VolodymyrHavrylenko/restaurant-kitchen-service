from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    fields = "__all__"


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 10

    def get_queryset(self):
        return Dish.objects.select_related("dish_type").prefetch_related(
            "ingredient",
            "cook"
        )


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 4
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 5


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")

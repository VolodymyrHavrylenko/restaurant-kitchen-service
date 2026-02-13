from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from kitchen.forms import CookCreateForm, DishCreateForm
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
    form_class = CookCreateForm

    def get_success_url(self):
        return reverse_lazy("kitchen:cook-detail", args=[self.object.id])

class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = ["first_name", "last_name", "year_of_experience"]

    def get_success_url(self):
        return reverse_lazy("kitchen:cook-detail", args=[self.object.id])


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")


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
    form_class = DishCreateForm

    def get_success_url(self):
        return reverse_lazy("kitchen:dish-detail", args=[self.object.id])


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishCreateForm

    def get_success_url(self):
        return reverse_lazy("kitchen:dish-detail", args=[self.object.id])


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


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


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/dish_type_confirm_delete.html"


class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 5


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredient-list")

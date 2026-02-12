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
    return render(request, 'kitchen/index.html', context=context)

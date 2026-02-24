from django import forms
from django.contrib.auth.forms import UserCreationForm

from kitchen.models import Cook, Dish, Ingredient


class CookCreateForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "year_of_experience",
        )


class DishCreateForm(forms.ModelForm):
    cook = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(), widget=forms.CheckboxSelectMultiple
     )
    ingredient = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Dish
        fields = "__all__"


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by Username"}),
    )


class SearchFormByName(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by Name"}),
    )

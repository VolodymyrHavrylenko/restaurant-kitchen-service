from django.test import TestCase
from django.contrib.auth import get_user_model

from kitchen.forms import CookCreateForm, DishCreateForm
from kitchen.models import DishType, Ingredient

User = get_user_model()


class CookCreateFormTest(TestCase):
    def test_form_is_valid_with_correct_data(self):
        """
        Verify the form is valid when all required fields are provided.
        """
        form_data = {
            "username": "cook1",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
            "first_name": "John",
            "last_name": "Doe",
            "year_of_experience": 5,
        }
        form = CookCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_requires_first_and_last_name(self):
        """
        Ensure the form is invalid without first and last name.
        """
        form_data = {
            "username": "cook1",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
            "year_of_experience": 5,
        }
        form = CookCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("first_name", form.errors)
        self.assertIn("last_name", form.errors)

    def test_form_saves_user_correctly(self):
        """
        Verify that a user is created and saved properly.
        """
        form_data = {
            "username": "cook2",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
            "first_name": "Jane",
            "last_name": "Smith",
            "year_of_experience": 3,
        }
        form = CookCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()

        self.assertEqual(user.username, "cook2")
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.year_of_experience, 3)
        self.assertTrue(user.check_password("StrongPass123"))


class DishCreateFormTest(TestCase):
    def setUp(self):
        """
        Create related objects required for the dish form.
        """
        self.user = User.objects.create_user(
            username="cook",
            password="test12345"
        )
        self.dish_type = DishType.objects.create(name="Main")
        self.ingredient1 = Ingredient.objects.create(name="Salt")
        self.ingredient2 = Ingredient.objects.create(name="Pepper")

    def test_form_is_valid_with_correct_data(self):
        """
        Verify the form is valid when correct data is provided.
        """
        form_data = {
            "name": "Steak",
            "description": "Test dish",
            "price": 25,
            "dish_type": self.dish_type.id,
            "cook": [self.user.id],
            "ingredient": [self.ingredient1.id, self.ingredient2.id],
        }
        form = DishCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_requires_related_fields(self):
        """
        Ensure the form is invalid if cooks or ingredients are missing.
        """
        form_data = {
            "name": "Steak",
            "description": "Test dish",
            "price": 25,
            "dish_type": self.dish_type.id,
        }
        form = DishCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("cook", form.errors)
        self.assertIn("ingredient", form.errors)

    def test_form_saves_dish_with_relations(self):
        """
        Verify a dish is saved with cooks and ingredients.
        """
        form_data = {
            "name": "Steak",
            "description": "Test dish",
            "price": 25,
            "dish_type": self.dish_type.id,
            "cook": [self.user.id],
            "ingredient": [self.ingredient1.id, self.ingredient2.id],
        }
        form = DishCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        dish = form.save()

        self.assertEqual(dish.name, "Steak")
        self.assertEqual(dish.dish_type, self.dish_type)
        self.assertEqual(dish.cook.count(), 1)
        self.assertEqual(dish.ingredient.count(), 2)

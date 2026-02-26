from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish, Ingredient


class TestModel(TestCase):
    def setUp(self):
        """
        Set up test data for DishType, Cook, Ingredient,
        and two Dish instances (with and without description).
        """
        self.dish_type = DishType.objects.create(
            name="test",
            )
        self.cook = get_user_model().objects.create_user(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
            year_of_experience=5,
        )
        self.ingredient = Ingredient.objects.create(
            name="test",
        )
        self.dish_with_description = Dish.objects.create(
            name="test_with_description",
            description="Test Description",
            dish_type=self.dish_type,
        )
        self.dish_with_description.ingredient.add(self.ingredient)
        self.dish_with_description.cook.add(self.cook)

        self.dish_without_description = Dish.objects.create(
            name="test_without_description",
            dish_type=self.dish_type,
        )
        self.dish_without_description.ingredient.add(self.ingredient)
        self.dish_without_description.cook.add(self.cook)

    def test_cook_str(self):
        """
        Test the __str__ method of Cook model.
        Should return: "username (first_name last_name) -
        year_of_experience years of experience".
        """
        self.assertEqual(
            str(self.cook),
            f"{self.cook.username} "
            f"({self.cook.first_name} {self.cook.last_name}) - "
            f"{self.cook.year_of_experience} years of experience"
        )

    def test_dish_type_str(self):
        """
        Test the __str__ method of DishType model.
        Should return the name of the dish type.
        """
        self.assertEqual(str(self.dish_type), self.dish_type.name)

    def test_dish_str_with_description(self):
        """
        Test the __str__ method of Dish model with description.
        Should return: "name - description".
        """
        self.assertEqual(
            str(self.dish_with_description),
            f"{self.dish_with_description.name} "
            f"- {self.dish_with_description.description}"
        )

    def test_dish_str_without_description(self):
        """
        Test the __str__ method of Dish model without description.
        Should return the name of the dish.
        """
        self.assertEqual(
            str(self.dish_without_description),
            self.dish_without_description.name
        )

    def test_ingredient_str(self):
        """
        Test the __str__ method of Ingredient model.
        Should return the name of the ingredient.
        """
        self.assertEqual(str(self.ingredient), self.ingredient.name)

    def test_create_cook_with_year_of_experience(self):
        """
        Test creating a Cook with a specific year_of_experience.
        Verifies username, year_of_experience, and password correctness.
        """
        cook = get_user_model().objects.get(username="test")
        self.assertEqual(cook.username, "test")
        self.assertEqual(cook.year_of_experience, 5)
        self.assertTrue(cook.check_password("test123"))

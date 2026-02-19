from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from kitchen.models import Dish, DishType, Ingredient

User = get_user_model()


class PublicViewsTest(TestCase):
    def test_index_view(self):
        """
        Verify that the home page is accessible to all users.
        """
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)

    def test_dish_list_view(self):
        """
        Ensure the dish list page is publicly accessible.
        """
        response = self.client.get(reverse("kitchen:dish-list"))
        self.assertEqual(response.status_code, 200)


class PrivateViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test12345"
        )
        self.client.force_login(self.user)

        self.dish_type = DishType.objects.create(name="Soup")
        self.ingredient = Ingredient.objects.create(name="Salt")
        self.dish = Dish.objects.create(
            name="Borscht",
            description="Test",
            price=10,
            dish_type=self.dish_type,
        )
        self.dish.ingredient.add(self.ingredient)
        self.dish.cook.add(self.user)

    def test_cook_list_view(self):
        """
        Check that logged-in users can access the cook list page.
        """
        response = self.client.get(reverse("kitchen:cook-list"))
        self.assertEqual(response.status_code, 200)

    def test_cook_detail_view(self):
        """
        Ensure a cook detail page loads correctly.
        """
        response = self.client.get(
            reverse("kitchen:cook-detail", args=[self.user.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_create_dish(self):
        """
        Verify that a dish can be created successfully.
        """
        response = self.client.post(
            reverse("kitchen:dish-create"),
            {
                "name": "Pizza",
                "description": "Test",
                "price": 20,
                "dish_type": self.dish_type.id,
                "ingredient": [self.ingredient.id],
                "cook": [self.user.id],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Dish.objects.filter(name="Pizza").exists())

    def test_update_dish(self):
        """
        Verify that an existing dish can be updated.
        """
        response = self.client.post(
            reverse("kitchen:dish-update", args=[self.dish.id]),
            {
                "name": "Updated",
                "description": "Test",
                "price": 15,
                "dish_type": self.dish_type.id,
                "ingredient": [self.ingredient.id],
                "cook": [self.user.id],
            },
        )
        self.dish.refresh_from_db()
        self.assertEqual(self.dish.name, "Updated")

    def test_delete_dish(self):
        """
        Ensure a dish can be deleted.
        """
        response = self.client.post(
            reverse("kitchen:dish-delete", args=[self.dish.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(id=self.dish.id).exists())

    def test_delete_dish_type_protected(self):
        """
        Ensure a dish type cannot be deleted if dishes depend on it.
        """
        response = self.client.post(
            reverse("kitchen:dish-type-delete", args=[self.dish_type.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(DishType.objects.filter(id=self.dish_type.id).exists())

    def test_ingredient_create(self):
        """
        Verify that a new ingredient can be created."""
        response = self.client.post(
            reverse("kitchen:ingredient-create"),
            {"name": "Pepper"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Ingredient.objects.filter(name="Pepper").exists())

    def test_ingredient_delete(self):
        """
        Ensure an ingredient can be deleted.
        """
        response = self.client.post(
            reverse("kitchen:ingredient-delete", args=[self.ingredient.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Ingredient.objects.filter(id=self.ingredient.id).exists())

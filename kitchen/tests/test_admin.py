from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import Dish, Ingredient, DishType


class CookAdminSiteTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="testcook",
            year_of_experience=5,
        )

    def test_cook_year_of_experience_listed(self):
        """
        Test that year_of_experience appears in admin changelist page.
        """
        url = reverse(
            "admin:kitchen_cook_changelist",
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cook.year_of_experience)

    def test_cook_detail_year_of_experience_listed(self):
        """
        Test that year_of_experience appears in admin detail page.
        """
        url = reverse(
            "admin:kitchen_cook_change",
            args=[self.cook.id],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cook.year_of_experience)

    def test_cook_add_page_year_of_experience_listed(self):
        """
        Test that year_of_experience appears in admin detail page.
        """
        url = reverse(
            "admin:kitchen_cook_add",
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "year_of_experience")

class DishAdminSiteTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)
        self.dish_type = DishType.objects.create(
            name="Test Type",
        )
        self.ingredient = Ingredient.objects.create(
            name="Test Ingredient",
        )
        self.dish = Dish.objects.create(
            name="Test Dish",
            dish_type=self.dish_type,
            description="Test description",
            price=5.0,
        )
        self.dish.ingredient.add(self.ingredient)
        self.dish.cook.add(self.admin_user)

    def test_dish_name_dish_type_price_description_listed(self):
        """
        Test that dish name, description, price,
        and dish type are displayed in admin changelist.
        """
        url = reverse(
            "admin:kitchen_dish_changelist",
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.dish.name)
        self.assertContains(response, self.dish.description)
        self.assertContains(response, str(self.dish.price))
        self.assertContains(response, str(self.dish.dish_type))

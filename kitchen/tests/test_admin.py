from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

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
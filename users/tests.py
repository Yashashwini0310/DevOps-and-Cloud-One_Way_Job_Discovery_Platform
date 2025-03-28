import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

@pytest.mark.django_db
class TestAccounts:
    def setup_method(self):
        """Create a test user"""
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@example.com",
            password="TestPassword123",
            first_name="Test",
            last_name="User",
            bio="Test Bio",
            location="Test Location",
            phone="123-456-7890",
        )

    def test_user_creation(self):
        """Test if a user is created successfully"""
        assert self.user.username == "testuser"
        assert self.user.email == "test@example.com"
        assert self.user.check_password("TestPassword123")

    def test_login(self, client):
        """Test if login works correctly"""
        login = client.login(username="testuser", password="TestPassword123")
        assert login is True

    def test_profile_update(self, client):
        """Test if a user can update their profile"""
        client.login(username="testuser", password="TestPassword123")
        response = client.get(reverse("users:edit_profile")) #get the edit profile page.
        csrf_token = response.context['csrf_token'] #get the csrf token.

        response = client.post(
            reverse("users:edit_profile"),
            {
                "username": "updateduser",
                "email": "updated@example.com",
                "first_name": "Updated",
                "last_name": "User",
                "bio": "Updated Bio",
                "location": "Updated Location",
                "phone": "987-654-3210",
                "csrfmiddlewaretoken": csrf_token,
            },
        )

        self.user.refresh_from_db()  # Refresh from DB after update
        assert self.user.username == "updateduser"
        assert self.user.email == "updated@example.com"
        assert self.user.first_name == "Updated"
        assert self.user.last_name == "User"
        assert self.user.bio == "Updated Bio"
        assert self.user.location == "Updated Location"
        assert self.user.phone == "987-654-3210"
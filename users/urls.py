from django.urls import path
from .views import register, login_view, logout_view, profile, edit_profile
app_name = 'users'
urlpatterns = [
    path('profile/', profile, name='profile'),
    path("profile/edit/", edit_profile, name="edit_profile"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]

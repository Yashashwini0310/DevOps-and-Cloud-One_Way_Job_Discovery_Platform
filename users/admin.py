"""Better user listing in the admin panel.
Allows searching users by email & username.
Shows account status & join date."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('-date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)

"""Better job listing view with filters.
Field grouping for better readability.
Ordering jobs by the latest postings.
"""
from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'posted_at')
    search_fields = ('title', 'company', 'location')
    list_filter = ('company', 'location', 'posted_at')
    ordering = ('-posted_at',)
    fieldsets = (
        ('Job Details', {'fields': ('title', 'company', 'location', 'salary', 'description')}),
        ('Additional Info', {'fields': ('posted_at',)}),
    )

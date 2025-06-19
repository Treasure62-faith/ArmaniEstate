from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_published', 'created_at')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'description', 'address')

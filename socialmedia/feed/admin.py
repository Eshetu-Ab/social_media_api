# In admin.py
from django.contrib import admin
from .models import FeedItem

@admin.register(FeedItem)
class FeedItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')



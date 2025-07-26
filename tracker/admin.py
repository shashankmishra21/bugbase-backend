from django.contrib import admin
from .models import Bug, Comment

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_by', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'created_by__username')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'bug', 'text', 'created_at']
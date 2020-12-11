from django.contrib import admin
from .models import Category, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'published', 'category')
    
admin.site.register(Category)

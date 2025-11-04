from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'is_published', 'views_count', )
    list_filter = ('views_count',)
    search_fields = ('title', 'content',)


from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Item


class ModelItemAdmin(admin.ModelAdmin):
    list_display = ('meal','category', 'price', 'status', 'author')
    list_filter = ('meal', 'description', 'price', 'category',
                   'status', 'author', 'date_created', 'date_updated')
    search_fields = ('meal', 'description', 'price', 'category')
    ordering = ('category',)


admin.site.register(Item, ModelItemAdmin)
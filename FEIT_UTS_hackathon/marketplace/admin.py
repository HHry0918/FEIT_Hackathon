from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'seller', 'student_id', 'description', 'date', 'status_verified', 'price')

admin.site.register(Item, ItemAdmin)


from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'item_name', 'seller', 'student_id', 'description', 'date', 'status_verified', 'price')
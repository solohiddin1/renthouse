from rest_framework import serializers
from app.models import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['name', 'location', 'image', 'owner', 'cost', 'open_time', 'close_time']
        read_only_fields = ['id','created_at', 'updated_at']
from rest_framework import serializers
from app.models import House, HouseImages

class HouseimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImages
        fields = ['images', 'house']

class HouseSerializer(serializers.ModelSerializer):
    images = HouseimageSerializer(required=False, many=True)
    class Meta:
        model = House
        fields = ['name', 'location', 'images', 'owner', 'cost']
        read_only_fields = ['id','created_at', 'updated_at']
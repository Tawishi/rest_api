from rest_framework import serializers

from apis.models import Restaurants


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['name', 'type', 'description']

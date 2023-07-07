from rest_framework import serializers
from api.models import Bikes

class BikeSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)

    class Meta:
        model=Bikes
        fields="__all__"


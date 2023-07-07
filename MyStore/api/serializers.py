from rest_framework import serializers
from api.models import Products

# class Productserializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     price=serializers.IntegerField()
#     category=serializers.CharField()
#     description=serializers.CharField()
#     is_active=serializers.BooleanField(read_only=True)

class Productserializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    is_active=serializers.BooleanField(read_only=True)
    class Meta:
        model=Products
        fields="__all__"

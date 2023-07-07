from rest_framework import serializers
from api.models import Books
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Books
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
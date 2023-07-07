from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import DoctorProfile,Department,DocLeave

class UserPatientSerialzer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email","first_name","last_name"]

        def create(self,validated_data):
            return User.objects.create_user(**validated_data)
        

class UserDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)
    

class DoctorProfileSerializer(serializers.ModelSerializer):
    user=UserDoctorSerializer(read_only=True,many=False)
    id=serializers.CharField(read_only=True)
    
    class Meta:
        model=DoctorProfile
        fields="__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    model=Department
    fields="__all__"


class DoctorLeaveSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)

    class Meta:
        model = DocLeave
        fields="__all__"
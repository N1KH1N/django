from django.shortcuts import render
from django.views.generic import View
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from rest_framework.viewsets import ViewSet,ModelViewSet,GenericViewSet
from api.serializers import DoctorLeaveSerializer, UserPatientSerialzer,UserDoctorSerializer,DoctorProfileSerializer,serializers,DepartmentSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from api.models import DoctorProfile,Department,DocLeave
from rest_framework import authentication,permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework import generics, permissions

# from django.core.mail import send_mail
# from django.conf import settings

class UserPatientView(ModelViewSet,GenericViewSet):
    serializer_class=UserPatientSerialzer
    queryset=User.objects.all()

class UserDoctorView(ModelViewSet,GenericViewSet):
    serializer_class=UserDoctorSerializer
    queryset=User.objects.all()   

class DoctorProfileView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=DoctorProfileSerializer
    queryset=DoctorProfile.objects.all()


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def destroy(self, request, *args, **kwargs):
        prf=self.get_object()
        if prf.user!=request.user:
            raise serializers.ValidationError("Action Not Allowed")
        else:
            print("Deleted Succesfully")
            return super().destroy(request,*args,**kwargs)
        
class DepartmentView(ModelViewSet):
    serializer_class=DepartmentSerializer
    model=Department
    queryset=Department.objects.all()



    @action(methods=["GET"],detail=False)
    def department(self,request,*args,**kwargs):
        qs=Department.objects.all().values_list("department_name",flat=True).distinct()
        return Response(data=qs)
    

    def get_queryset(self):
        qs=Department.objects.all()
        if "department_name" in self.request.query_params:
            cat=self.request.query_params.get("department_name")
            qs=qs.filter(department_name=cat)
        return qs
    



class DoctorLeaveListCreate(ModelViewSet):
    serializer_class = DoctorLeaveSerializer
    permission_classes = [permissions.IsAuthenticated]
    # queryset=DoctorProfile.objects.all()

    @action(methods=["post"],detail=True)
    def doctorleave(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        doc=DoctorProfile.objects.get(id=id)
        serializer=DoctorLeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(doctor=doc,user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import BikeSerializer
from api.models import Bikes

class BikesView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Bikes.objects.all()
        serializer=BikeSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class BikeDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Bikes.objects.get(id=id)
        serializer=BikeSerializer(obj,many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Bikes.objects.get(id=id)
        serializer=BikeSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Bikes.objects.get(id=id).delete()
        return Response(data="DELETED !!!")
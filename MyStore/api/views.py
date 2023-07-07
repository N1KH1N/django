from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from api.models import Products
from api.serializers import Productserializer

# products CRUD
# class ProductsView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response(data="list all products")
#     def post(self,request,*args,**kwargs):
#         return Response(data="creating product")
#
# class ProductDetailsView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response(data="detail of a product with given id")
#     def put(self,request,*args,**kwargs):
#         return Response(data="updating product")
#     def delete(self,request,*args,**kwargs):
#         return Response(data="deleting object")


class ProductsView(APIView):

    def get(self,request,*args,**kwargs):
        qs=Products.objects.all() #type of qs set => [{}],[],{}
        if "category" in request.query_params:
            cat=request.query_params.get("category")
            qs=qs.filter(category=cat)
        if "price_gt" in request.query_params:
            pr=request.query_params.get("price_gt")
            qs=qs.filter(price__gt=pr)
        if "price_lt" in request.query_params:
            pr=request.query_params.get("price_lt")
            qs=qs.filter(price__lt=pr)
        if "limit" in request.query_params:
            lm=request.query_params.get("limit")
            qs=qs[:int(lm)]


        sz=Productserializer(qs,many=True)
        return Response(data=sz.data) #Response()=>json(qs)


    def post(self,request,*args,**kwargs):
        serializer=Productserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=Productserializer(qs,many=False)
        return Response(data=serializer.data)


    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Products.objects.get(id=id)
        serializer=Productserializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Products.objects.get(id=id).delete()
        return Response(data="deleted")

class CategoryViews(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all().values_list("category",flat=True).distinct()
        return Response(data=qs)
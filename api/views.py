from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import category_s, b_ser, pro_ser
import django_filters
class cat_list(generics.ListCreateAPIView):
     queryset = Category.objects.all()
     serializer_class = category_s
     def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
               return Category.objects.filter(title__icontains=name) 
        return queryset

class cat_detail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Category.objects.all()
     serializer_class = category_s
     lookup_field = "pk"

class brand_list(generics.ListCreateAPIView):
     queryset = Brand.objects.all()
     serializer_class = b_ser

     def get_queryset(self):
        queryset = Brand.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
               return Brand.objects.filter(title__icontains=name) 
        return queryset
     
class brand_detail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Brand.objects.all()
     serializer_class = b_ser
     lookup_field = "pk"

class product_list(generics.ListCreateAPIView):
     queryset = Product.objects.all()
     serializer_class = pro_ser

class pro_detail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Product.objects.all()
     serializer_class = pro_ser
     lookup_field = "pk"
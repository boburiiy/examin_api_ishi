from rest_framework import serializers
from .models import Category, Brand, Product

class category_s(serializers.ModelSerializer):
     class Meta:
          model = Category
          fields = ('id', 'title', 'slug')

class b_ser(serializers.ModelSerializer):
     class Meta:
          model = Brand
          fields = ('id', 'title')

class pro_ser(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = ('id', 'title', 'desc', 'image', 'price', 'cat_id', 'brand_id')
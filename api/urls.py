from django.urls import path
from .views import *
from django.conf import settings
urlpatterns = [
     path('categories/', cat_list.as_view()),
     path('brands/', brand_list.as_view()),
     path('categories/<int:pk>/', cat_detail.as_view()),
     path('brands/<int:pk>/', brand_detail.as_view()),
     path('products/', product_list.as_view()),
     path('products/<int:pk>/', pro_detail.as_view()),
]

if settings.DEBUG:
    urlpatterns
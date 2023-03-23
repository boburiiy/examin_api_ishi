from django.contrib import admin
from .models import *
reg = admin.site.register

reg(Category)
reg(Brand)
reg(Product)
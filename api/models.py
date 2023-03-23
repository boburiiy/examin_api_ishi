from django.db import models
class Category(models.Model):
     title = models.CharField(max_length=100)
     slug = models.SlugField(unique=True)

     def __str__(self):
         return self.title
class Brand(models.Model):
     title = models.CharField(max_length=100)

     def __str__(self):
         return self.title
class Product(models.Model):
     title = models.CharField(max_length=100)
     desc = models.TextField()
     image = models.ImageField(upload_to='media/')
     price = models.DecimalField(max_digits=10, decimal_places=2)
     cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
     brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)

def __str__(self):
    return self.title
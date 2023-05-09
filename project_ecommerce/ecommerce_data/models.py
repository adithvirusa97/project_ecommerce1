from django.db import models

# Create your models here.

class Categories(models.Model):
    category_name = models.CharField(max_length=255,blank=False,null=False)
    # category_description = models.TextField(max_length=255,null = True,Blank=True)
    def __str__(self):
        return self.category_name
class SubCategories(models.Model):
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=255,blank=False,null=False)
    # category_description = models.TextField(max_length=255,null = True,Blank=True)

class Products(models.Model):
    sub_category = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255,blank=False,null=False)
    Price = models.FloatField(max_length=20,null=False, blank=False)
    Quantity = models.IntegerField(null=False,blank=False,)
    Image = models.ImageField(upload_to='products',blank=False,null=False)

from django.db import models


class Product(models.Model):
    # product_id = models.AutoField
    product_name = models.CharField(max_length=200)
    filpkart_id = models.CharField(max_length=700,default="")
    amazon_id = models.CharField(max_length=700, default="")
    # category = models.CharField(max_length=50, default="")
    # subcategory = models.CharField(max_length=50, default="")
    # price = models.IntegerField(default=0)
    # desc = models.CharField(max_length=300)
    # pub_date = models.DateField()
    # image = models.ImageField(upload_to="Hetul11/images", default="")



    def __str__(self):
        return self.product_name

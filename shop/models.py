from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    catagory = models.CharField(max_length= 30, default='')
    sub_catagory = models.CharField(max_length= 30, default='')
    product_decs = models.CharField(max_length = 300)
    pub_date = models.DateField()
    product_img = models.ImageField(upload_to='shop/image', default='')


    def __str__(self):
        return self.product_name

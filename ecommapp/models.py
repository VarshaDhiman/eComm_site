from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    desc = models.TextField(max_length=240)
    phoneNumber = models.IntegerField(max_length=10)

    def __init__(str):
        return self.id


class Producat(models.Model):
    producat_id = models.AutoField
    producat_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'images/images')

    def __str__(self):
        return self.producat_name
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code =  models.CharField(max_length=50)
    oid =  models.CharField(max_length=50, blank=True)
    amountpaid = models.CharField(max_length=400,blank=True,null=True)
    paymentstatus =  models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=100,default="")


    def __str__(self):
        return self.name
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntergerField(default = "")
    update_desc = models.TextField(max_length=300)
    delivered = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.update_desc[0:7]+"...."
    
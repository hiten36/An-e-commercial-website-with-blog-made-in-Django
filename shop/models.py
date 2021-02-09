from django.db import models

# Create your models here.
class product(models.Model):
    prod_id=models.AutoField
    prod_name=models.CharField(max_length=50)
    prod_desc=models.CharField(max_length=2000)
    prod_price=models.CharField(max_length=50)
    prod_cat=models.CharField(max_length=40,default='')
    prod_sub_cat=models.CharField(max_length=70)
    pub_date=models.DateField()
    prod_image=models.ImageField(upload_to="shop/images")

    def __str__(self):
        return self.prod_name

class contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=80,default='')
    phone=models.IntegerField(default='')
    desc=models.CharField(max_length=2000,default='')

    def __str__(self):
        return self.name

class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=3000)
    price=models.CharField(max_length=100,default='')
    name=models.CharField(max_length=80)
    email=models.CharField(max_length=80)
    phone=models.IntegerField(default=0)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=10)


    def __str__(self):
        return self.name
class orderupdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.CharField(max_length=100,default='')
    update_desc=models.CharField(max_length=2000)
    ts=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:15]+' ...'
from django.db import models
from django.contrib import admin

class Amazon(models.Model):
    seller_id=models.CharField(max_length=30)
    manufacture_date=models.IntegerField()
    product_name=models.CharField(max_length=30)
    expiry_date=models.IntegerField()
    price=models.IntegerField()

class AmazonAdmin(admin.ModelAdmin):
    list_display=('seller_id', 'manufacture_date', 'product_name', 'expiry_date', 'price')


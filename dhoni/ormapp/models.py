from django.db import models
from django.contrib import admin
class eprod(models.Model):
    p_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    price = models.FloatField()
    del_date = models.DateField()
    del_charge = models.FloatField()
    rating = models.FloatField()
    del_stock = models.CharField(max_length=100)
class eprodAdmin(admin.ModelAdmin):
    list_display = ["p_id","name","price","del_date","del_charge","rating","del_stock"]


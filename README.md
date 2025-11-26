# Ex01 Django ORM Web Application
## Date: 26/11/2025

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
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


from django.contrib import admin
from.models import eprod,eprodAdmin
admin.site.register(eprod,eprodAdmin)
```


## OUTPUT
![alt text](<Screenshot (5)-1.png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully

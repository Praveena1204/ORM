# Ex02 Django ORM Web Application
## Date: 
16-11-24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<project web.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

from django.db import models
from django.contrib import admin
class customer (models.Model):
    c_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
 
class customerAdmin(admin.ModelAdmin):
    list_display=('c_id','name','salary','age','email')
 
admin.py

from django.contrib import admin
from .models import customer,customerAdmin
admin.site.register(customer,customerAdmin)
```




## OUTPUT
![alt text](<Screenshot 2024-11-16 091430.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully

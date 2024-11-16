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
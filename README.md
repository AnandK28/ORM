# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![Alt text](Untitled-1.png)

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
from django.contrib import adming
class Bank(models.Model):
	Name=models.CharField(max_length=20)
	AccNo=models.IntegerField(primary_key="AccNo")
	LoanAmt=models.IntegerField()
	Interest=models.IntegerField()
class BankAdmin(admin.ModelAdmin):
	list_display=('Name','AccNo','LoanAmt','Interest')
	
admin.py

from django.contrib import admin
from .models import Bank,BankAdmin
admin.site.register(Bank,BankAdmin)


```


## OUTPUT

![Alt text](<Screenshot 2024-10-26 141903.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully

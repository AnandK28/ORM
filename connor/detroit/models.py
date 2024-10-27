from django.db import models
from django.contrib import admin
class Bank(models.Model):
	Name=models.CharField(max_length=20)
	AccNo=models.IntegerField(primary_key="AccNo")
	PhoneNo=models.IntegerField(max_length=10)
	LoanAmt=models.IntegerField()
	Interest=models.IntegerField()
class BankAdmin(admin.ModelAdmin):
	list_display=('Name','AccNo','PhoneNo','LoanAmt','Interest')

from django.db import models
from django.contrib import adming
class Bank(models.Model):
	Name=models.CharField(max_length=20)
	AccNo=models.IntegerField(primary_key="AccNo")
	LoanAmt=models.IntegerField()
	Interest=models.IntegerField()
class BankAdmin(admin.ModelAdmin):
	list_display=('Name','AccNo','LoanAmt','Interest')
	
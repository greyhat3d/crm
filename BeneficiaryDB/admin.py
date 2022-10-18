from django.contrib import admin
from .models import Beneficiary
# Register your models here.

class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('id', "firstname", "lastname")
    
admin.site.register(Beneficiary, BeneficiaryAdmin)
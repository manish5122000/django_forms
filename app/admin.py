from django.contrib import admin
from .models import AccountDetails

# Register your models here.

@admin.register(AccountDetails)
class AccouuntDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'locality', 'city', 'zipcode', 'state', 'Account_Number', 'IFSC_Code']
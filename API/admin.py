from django.contrib import admin
from .models import RAMStatus

@admin.register(RAMStatus)
class RAMStatusAdmin(admin.ModelAdmin):
    list_display = ('report_date', 'total', 'free', 'used')

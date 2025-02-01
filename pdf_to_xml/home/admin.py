from django.contrib import admin
from .models import LcData

# Register your models here.

class LcDataAdmin(admin.ModelAdmin):
    list_display=('lc_number','date_of_issue','expiry_date','applicant')

admin.site.register(LcData,LcDataAdmin)
from django import forms
from .models import LcData

class LcDataUploadForm(forms.ModelForm):
    class Meta:
        model= LcData
        fields=['lc_number','date_of_issue','expiry_date','applicant','beneficiary','currency','amount','tenor']

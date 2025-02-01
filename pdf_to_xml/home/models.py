from django.db import models

# Create your models here.

class LcData(models.Model):
    lc_number=models.CharField(max_length=13,null=True)
    date_of_issue=models.CharField(max_length=6,null=True)
    expiry_date=models.CharField(max_length=6,null=True)
    applicant=models.CharField(max_length=50,null=True)
    beneficiary=models.CharField(max_length=50,null=True)
    currency=models.CharField(max_length=3,null=True)
    amount=models.CharField(max_length=8,null=True)
    tenor=models.CharField(max_length=3,null=True)


    def __str__(self):
        return self.lc_number

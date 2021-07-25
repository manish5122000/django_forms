# from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATE_CHOICES = (
    ('Andaman & Nicobar Island','Andaman & Nicobar Island'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman & Diu','Daman & Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujrat','Gujrat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadeep','Lakshadeep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharastra','Maharastra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
)

class AccountDetails(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    locality = models.CharField(max_length=200, default='1')
    city = models.CharField(max_length=200, default='1')
    zipcode = models.IntegerField(default='1')
    state = models.CharField(choices=STATE_CHOICES, default='Delhi', max_length=50)
    Account_Number = models.CharField(max_length=30,null=True)
    IFSC_Code = models.CharField(max_length=20,null=True)

   


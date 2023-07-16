from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from base import BaseModel
from inventory import Cuvee

class Organization(BaseModel):
    pass

class Vendor(BaseModel):
    name = models.CharField(max_length=64)

class Member(BaseModel):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    cell_number = PhoneNumberField(null=True, blank=True, unique=True)  # https://django-phonenumber-field.readthedocs.io/en/latest/
    tried_cuvees = models.ForeignKey(to=Cuvee, on_delete=models.CASCADE)


from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from inventory.models.base import BaseModel


class Organization(BaseModel):
    pass


class Vendor(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class Member(BaseModel):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    # https://django-phonenumber-field.readthedocs.io/en/latest/
    cell_number = PhoneNumberField(null=True, blank=True, unique=True)
    tried_cuvees = models.ForeignKey(
        to='inventory.Cuvee',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'

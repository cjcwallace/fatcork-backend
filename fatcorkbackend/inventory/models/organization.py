from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from inventory.models.base import BaseModel


class Organization(BaseModel):
    """
    fatcork? otherworld? We can assign users an organization? This would allow us to scale the project to multiple wine shops
    multiple apps, one for each shop?
    """
    pass


class Vendor(BaseModel):
    """
    This doesn't really belong in this class file, find a place to move it to

    more information would be nice:
        -region
        -start date
        -??
        -blurb thats on the tasting cards?
    """
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


"""
We want to use the User class instead of Member class
"""
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

from django.db import models
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager

from organization import Vendor

class ProductType(models.TextChoices):
    STANDARD = 'ST', _('Standard')
    LARGE_FORMAT = 'LF', _('Large Format')
    HALF_BOTTLES = 'HB', _('Half bottles')
    WINE = 'WI', _('Wine')

class ProductStatus(models.TextChoices):
    ACTIVE = 'AC', _('Active')
    DRAFT = 'DR', _('Draft')
    ARCHIVED = 'AR', _('Archived')

class Product(models.model):
    handle = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    vendor = models.ForeignKey(to=Vendor, on_delete=models.CASCADE)
    product_category = models.CharField(max_length=256)
    type = models.CharField(max_length=2, choices=ProductType.choices, default=ProductType.STANDARD)
    tags = TaggableManager(null=True, blank=True)  # https://django-taggit.readthedocs.io/en/stable/api.html
    published = models.BooleanField(default=False, null=True, blank=True)
    variant_sku = models.CharField(max_length=32)
    variant_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    variant_compare_at_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_src = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=ProductStatus.choices, default=ProductStatus.ACTIVE, null=True, blank=True)

class Cuvee(Product):
    vintage = models.CharField(max_length=128)
    alcohol_pct = models.SmallIntegerField()
    varietal = models.CharField(max_length=128)
    village = models.CharField(max_length=128)
    disgorgement = models.DateField()
    dosage = models.SmallIntegerField()
    see = models.CharField(max_length=256, null=True, blank=True)
    smell = models.CharField(max_length=256, null=True, blank=True)
    taste = models.CharField(max_length=256, null=True, blank=True)
    pair = models.CharField(max_length=256, null=True, blank=True)
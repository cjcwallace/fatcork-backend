from django.db import models
from django.utils.translation import gettext_lazy as _

# from taggit.managers import TaggableManager

from inventory.models.organization import Vendor
from inventory.models.base import BaseModel


class ProductType(models.TextChoices):
    STANDARD = 'ST', _('Standard')
    LARGE_FORMAT = 'LF', _('Large Format')
    HALF_BOTTLES = 'HB', _('Half bottles')
    WINE = 'WI', _('Wine')


class ProductStatus(models.TextChoices):
    ACTIVE = 'AC', _('Active')
    ARCHIVED = 'AR', _('Archived')
    DRAFT = 'DR', _('Draft')
    NONE = 'NA', _('None')


class Product(BaseModel):
    handle = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    vendor = models.ForeignKey(to=Vendor, on_delete=models.CASCADE)
    product_category = models.CharField(max_length=256)
    type = models.CharField(
        max_length=2,
        choices=ProductType.choices,
        default=ProductType.STANDARD,
    )
    # https://django-taggit.readthedocs.io/en/stable/api.html
    # tags = TaggableManager(blank=True)
    published = models.BooleanField(default=False, null=True, blank=True)
    variant_sku = models.CharField(max_length=32)
    variant_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    variant_compare_at_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
    )
    image_src = models.URLField(null=True, blank=True)
    status = models.CharField(
        max_length=2,
        choices=ProductStatus.choices,
        default=ProductStatus.ACTIVE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.title}'


class Cuvee(Product):
    """
    future proofing fields: alcohol_pct

    TODO: can we populate the 'pair' field and create queries on it?
    """
    vintage = models.CharField(max_length=128, null=True, blank=True)
    alcohol_pct = models.SmallIntegerField(null=True, blank=True)
    varietal = models.CharField(max_length=128, null=True, blank=True)
    village = models.CharField(max_length=128, null=True, blank=True)
    disgorgement = models.DateField(null=True, blank=True)
    dosage = models.SmallIntegerField(null=True, blank=True)
    see = models.CharField(max_length=256, null=True, blank=True)
    smell = models.CharField(max_length=256, null=True, blank=True)
    taste = models.CharField(max_length=256, null=True, blank=True)
    pair = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

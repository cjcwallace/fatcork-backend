from django.db import models as django_models

from inventory.utilities.data import encrypt_value


class HashField(django_models.CharField):
    """
    Subclass of the CharField that stores the value as a hash
    """

    description = "CharField that stores the value as a hash"

    def get_prep_value(self, value):
        if value is None:
            return ''

        return encrypt_value(value)

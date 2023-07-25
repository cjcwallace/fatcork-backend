from django.conf import settings
from django.db import models

from inventory.middleware import get_api_current_user

USER_FK_ARGS = (settings.AUTH_USER_MODEL, models.SET_NULL)
USER_FK_KWARGS = {
    'blank': True,
    'null': True,
    'default': get_api_current_user,
    'editable': False,
    'related_name': '+',
}


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(*USER_FK_ARGS, **USER_FK_KWARGS)
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(*USER_FK_ARGS, **USER_FK_KWARGS)

    def save(self, *args, **kwargs):
        self.modified_by_id = get_api_current_user()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True

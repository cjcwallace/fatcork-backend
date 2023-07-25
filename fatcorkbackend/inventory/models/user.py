from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from encrypted_model_fields.fields import EncryptedCharField, EncryptedEmailField

from inventory.utilities import HashField


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email).lower()
        user = self.model(email=email, email_hash=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email_hash, password=None, **extra_fields):
        return self._create_user(email_hash, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = EncryptedCharField(_('first name'), max_length=30, blank=True)
    last_name = EncryptedCharField(_('last name'), max_length=150, blank=True)
    email = EncryptedEmailField(_('Email Address'), unique=True)
    email_hash = HashField(_('Email Address'), max_length=125, unique=True)

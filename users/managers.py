from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    
    def createUser(self, phoneNumber, password, **extra_fields):
        if not phoneNumber:
            raise ValueError(_("a phone number is required"))
        user = self.model(phoneNumber, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import datetime
from users.managers import UserManager

#class User(AbstractBaseUser, PermissionsMixin):
class User(models.Model):
    createdBy = models.CharField(max_length=70, blank=False, default='')
    createdDay = models.IntegerField(blank=False, default=1)
    createdMonth = models.IntegerField(blank=False, default=1)
    createdYear = models.IntegerField(blank=False, default=2022)
    createdAt = models.DateTimeField(default=datetime.datetime.now())
    firstName = models.CharField(max_length=70, blank=False, default='')
    lastName = models.CharField(max_length=70, blank=False, default='')
    phoneNumber = models.CharField(max_length=70, blank=False, default='')
    emailAddress = models.EmailField(max_length=70, blank=False)
    countryCode = models.CharField(max_length=70, blank=False, default='')
    maritalStatus = models.CharField(max_length=70, blank=False, default='')
    gender = models.CharField(max_length=70, blank=False, default='')
    dateOfBirth = models.CharField(max_length=70, blank=False, default='')
    userType = models.CharField(max_length=70, blank=False, default='')
    isDeleted = models.BooleanField(default=False)
    stateOfResidence = models.CharField(max_length=250, blank=False, default='')
    city = models.CharField(max_length=250, blank=False, default='')
    address = models.CharField(max_length=250, blank=False, default='')
    nOKFullName = models.CharField(max_length=70, blank=False, default='')
    nOKRelationship = models.CharField(max_length=70, blank=False, default='')
    nOKEmailAddress = models.CharField(max_length=70, blank=False, default='')
    nOKPhoneNumber = models.CharField(max_length=70, blank=False, default='')
    nOKAddress = models.CharField(max_length=250, blank=False, default='')
    pin = models.IntegerField(blank=False, default=0000)
    password = models.CharField(max_length=250, blank=False, default='')
    fileUrl = models.TextField(blank=False, default='')
    fileName = models.TextField(blank=False, default='')
    originalFileName = models.TextField(blank=False, default='')

    # USERNAME_FIELD="phoneNumber"

    # objects = UserManager()

    # def __str__(self):
    #    return self.phoneNumber
    
    # def tokens(self):
    #    pass
    
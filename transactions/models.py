import datetime
from django.db import models

class TransactionData(models.Model):
    variation_id = models.CharField(max_length=250, blank=False, default='')
    network = models.CharField(max_length=70, blank=False, default='')
    phone = models.CharField(max_length=70, blank=False, default='')
    amount = models.CharField(max_length=70, blank=False, default='')
    cable_tv = models.CharField(max_length=70, blank=False, default='')
    subscription_plan = models.CharField(max_length=70, blank=False, default='')
    smartcard_number = models.CharField(max_length=70, blank=False, default='')
    amount_charged = models.CharField(max_length=70, blank=False, default='')
    service_fee = models.CharField(max_length=70, blank=False, default='')
    electricity = models.CharField(max_length=70, blank=False, default='')
    service_fee = models.CharField(max_length=70, blank=False, default='')
    meter_number = models.CharField(max_length=70, blank=False, default='')
    token = models.CharField(max_length=70, blank=False, default='')
    units = models.CharField(max_length=70, blank=False, default='')
    order_id = models.CharField(max_length=70, blank=False, default='')
    service_id = models.CharField(max_length=70, blank=False, default='')

class Transaction(models.Model):
    createdBy = models.CharField(max_length=70, blank=False, default='')
    createdAt = models.DateTimeField(default=datetime.datetime.now())
    isDeleted = models.BooleanField(default=False)
    order_id = models.CharField(max_length=70, blank=False, default='')
    code = models.CharField(max_length=70, blank=False, default='')
    message = models.CharField(max_length=70, blank=False, default='')
    data = models.ForeignKey(TransactionData, on_delete=models.CASCADE)
    status = models.CharField(max_length=70, blank=False, default='')
    previous = models.FloatField(default=0)
    current = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    serviceType = models.CharField(max_length=70, blank=False, default='')

from rest_framework import serializers 
from transactions.models import Transaction, TransactionData
 
class TransactionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionData
        fields = ('id',
                  'variation_id',
                  'network',
                  'phone',
                  'amount',
                  'cable_tv',
                  'subscription_plan',
                  'smartcard_number',
                  'amount_charged',
                  'service_fee',
                  'electricity',
                  'meter_number',
                  'token',
                  'units',
                  'order_id',
                  'service_id')
 
class TransactionSerializer(serializers.ModelSerializer):
 
    data = TransactionDataSerializer()
    class Meta:
        model = Transaction
        fields = ('id',
                  'createdBy',
                  'createdAt',
                  'isDeleted',
                  'order_id',
                  'code',
                  'message',
                  'data',
                  'status',
                  'previous',
                  'current',
                  'amount',
                  'serviceType')
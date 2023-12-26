from rest_framework import serializers 
from users.models import User
 
 
class UserSerializer(serializers.ModelSerializer):
 
 
    class Meta:
        model = User
        fields = ('id',
                  'createdBy',
                  'createdDay',
                  'createdYear',
                  'createdAt',
                  'firstName',
                  'lastName',
                  'phoneNumber',
                  'emailAddress',
                  'countryCode',
                  'maritalStatus',
                  'gender',
                  'dateOfBirth',
                  'userType',
                  'isDeleted',
                  'stateOfResidence',
                  'city',
                  'address',
                  'nOKFullName',
                  'nOKRelationship',
                  'nOKEmailAddress',
                  'nOKPhoneNumber',
                  'nOKAddress',
                  'pin',
                  'password',
                  'fileUrl',
                  'fileName',
                  'originalFileName')
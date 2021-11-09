from rest_framework import serializers
from django.contrib.auth.models import User
from .models import EmployeeBasicInfo

class EmployeeBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBasicInfo
        fields = '__all__'
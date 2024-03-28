from rest_framework import serializers
from assetApp.models import Company, Employee, Asset, AssetMsg

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class AssetMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMsg
        fields = '__all__'

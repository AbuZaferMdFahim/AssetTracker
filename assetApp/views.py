from rest_framework import generics
from assetApp.models import Company, Employee, Asset, AssetMsg
from assetApp.serializers import CompanySerializer, EmployeeSerializer, AssetSerializer, AssetMsgSerializer

class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AssetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetMsgListCreateAPIView(generics.ListCreateAPIView):
    queryset = AssetMsg.objects.all()
    serializer_class = AssetMsgSerializer



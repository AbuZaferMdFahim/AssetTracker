from django.urls import path
from assetApp.views import CompanyListCreateAPIView, EmployeeListCreateAPIView, AssetListCreateAPIView, AssetMsgListCreateAPIView

urlpatterns = [
    path('company/', CompanyListCreateAPIView.as_view(), name='company'),
    path('employee/', EmployeeListCreateAPIView.as_view(), name='employee'),
    path('asset/', AssetListCreateAPIView.as_view(), name='asset'),
    path('assetMsg/', AssetMsgListCreateAPIView.as_view(), name='assetMsg'),
]
from django.contrib import admin
from assetApp.models import Company,Employee,Asset,AssetMsg

# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Asset)
admin.site.register(AssetMsg)

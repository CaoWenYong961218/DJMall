from django.contrib import admin
from .models import DJMallProductSPUCarouse

class DJMallProductSPUCarouseInlineAdmin(admin.TabularInline):
    model = DJMallProductSPUCarouse
    extra = 3
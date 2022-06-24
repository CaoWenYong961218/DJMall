from django.contrib import admin
from apps.dadmin.admin import admin_site
from .models import DJMallProductCategory, DJMallProductBrand, DJMallProductSPU
from .inline_admin import DJMallProductSPUCarouseInlineAdmin

@admin.register(DJMallProductCategory, site=admin_site)
class DJMallProductCategoryAdmin(admin.ModelAdmin):
    '''Admin View for DJMallProductCategor'''
    list_display = ('id', 'name', 'parent', 'add_date')
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(DJMallProductBrand, site=admin_site)
class DJMallProductBrandAdmin(admin.ModelAdmin):
    '''Admin View for DJMallProductBrand'''
    list_display = ('id', 'name', 'add_date')
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(DJMallProductSPU, site=admin_site)
class DJMallProductSPUAdmin(admin.ModelAdmin):
    '''Admin View for DJMallProductSPU'''
    list_display = ('id', 'title', 'add_date')
    list_filter = ('title',)
    search_fields = ('title',)
    inlines = [DJMallProductSPUCarouseInlineAdmin]
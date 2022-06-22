from django.contrib import admin
from django.contrib.admin import AdminSite
# Register your models here.

class DJMallAdminSite(AdminSite):
    
    site_header = 'DJMall商城系统'
    site_title = '商城系统'
    login_template = 'dadmin/login.html'

admin_site = DJMallAdminSite(name='dadmin')
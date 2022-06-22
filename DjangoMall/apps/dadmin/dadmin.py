from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .admin import admin_site

User = get_user_model()

admin_site.register(User)
admin_site.register(Group)
from django.contrib import admin
from django.contrib.auth.models import Group

from items.models import Item


admin.site.register(Item)
admin.site.unregister(Group)

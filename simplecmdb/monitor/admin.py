from django.contrib import admin
from .models import Host
# Register your models here.

class HostAdmin(admin.ModelAdmin):
	list_display = ['util','mac','ip']

admin.site.register(Host, HostAdmin)

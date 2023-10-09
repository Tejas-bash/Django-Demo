from django.contrib import admin
from App.models import DemoForm

@admin.register(DemoForm)
class DemoAdminPanel(admin.ModelAdmin):
    list_display = ['Name']
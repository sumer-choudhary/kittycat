from django.contrib import admin
from Info.models import Info

# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ("name","email","password","rpassword")

admin.site.register(Info,InfoAdmin)

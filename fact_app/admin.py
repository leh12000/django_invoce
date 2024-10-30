from django.contrib import admin
from .models import *
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','address',"sex")



admin.site.register(Customer,CustomerAdmin)
admin.site.register(Invoice)
admin.site.register(Article)
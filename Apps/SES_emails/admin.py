from django.contrib import admin

from models import SuppressedList

class SuppressedListAdmin(admin.ModelAdmin):
    list_display = ['email','blocked']
    pass


admin.site.register(SuppressedList,SuppressedListAdmin)

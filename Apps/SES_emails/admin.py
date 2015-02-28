from django.contrib import admin
from models import SuppressedList, AWSSubscription


class SuppressedListAdmin(admin.ModelAdmin):
    list_display = ['email', 'blocked']
    pass


class AWSSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['link', 'created_at']
    pass

admin.site.register(SuppressedList, SuppressedListAdmin)
admin.site.register(AWSSubscription, AWSSubscriptionAdmin)
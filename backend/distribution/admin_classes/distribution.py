from django.contrib import admin

from log.services.commands import send_messages


class DistributionAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    actions = (send_messages,)

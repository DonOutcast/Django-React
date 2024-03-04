from django.contrib import admin


class MessageLogAdmin(admin.ModelAdmin):
    list_display = ("status", "sent_time",)

from django.contrib import admin
from log.models import MessageLog


@admin.action(description='Send messages to selected distributions')
def send_messages(modeladmin, request, queryset):
    for distribution in queryset:
        for user in distribution.users.all():
            MessageLog.objects.create(distribution=distribution, user=user, status=MessageLog.States.SEND)
    modeladmin.message_user(request, "Messages were sent successfully.")

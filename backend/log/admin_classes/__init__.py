from django.contrib import admin

from log.admin_classes.message_log import MessageLogAdmin
from log.models import MessageLog

admin.site.register(MessageLog, MessageLogAdmin)
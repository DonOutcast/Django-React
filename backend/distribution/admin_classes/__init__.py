from django.contrib import admin

from distribution.admin_classes.distribution import DistributionAdmin
from distribution.models import Distribution

admin.site.register(Distribution, DistributionAdmin)

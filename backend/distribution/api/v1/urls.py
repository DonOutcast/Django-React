from django.urls import path
from rest_framework.routers import DefaultRouter

from distribution.api.v1.views import DistributionViewSet


router = DefaultRouter()
router.register(r'', DistributionViewSet)
urlpatterns = (
    path('distribution/', DistributionViewSet.as_view({'get': 'list'}), name='distribution-list'),
    path('distribution/<int:pk>/statistics/', DistributionViewSet.as_view({'get': 'statistics'}), name='distribution-statistics'),
)

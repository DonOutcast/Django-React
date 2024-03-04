import factory

from core.factories import UserFactory
from distribution.models import Distribution


class DistributionFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Distribution

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action

from distribution.models import Distribution
from distribution.api.v1.serializers import DistributionSerializer
from log.models import MessageLog


class DistributionViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer

    @action(["GET"], detail=True)
    def statistics(self, request, pk=None):
        distribution = self.get_object()
        total_users = distribution.users.count()
        messages_sent = distribution.messages.filter(status=MessageLog.States.SEND).count()

        data = {
            "total_users": total_users,
            "messages_sent": messages_sent,
        }
        return Response(data)

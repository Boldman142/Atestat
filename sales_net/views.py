from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from users.models import User
from sales_net.models import SalesNet
from products.permissions import IsAdmin, IsOwner
from sales_net.serliazers import SalesNetSerializer
from sales_net.filters import SalesNetFilter


class SalesNetViewSet(viewsets.ModelViewSet):
    queryset = SalesNet.objects.all()
    serializer_class = SalesNetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SalesNetFilter

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        sales_net = serializer.save()
        sales_net.author = get_object_or_404(User, id=self.request.user.id)
        sales_net.save()

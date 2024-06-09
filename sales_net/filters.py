import django_filters
from sales_net.models import SalesNet


class SalesNetFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = SalesNet
        fields = ['city']

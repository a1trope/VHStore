import django_filters
from . import models


class CassetteFilter(django_filters.FilterSet):
    class Meta:
        model = models.Cassette
        fields = ["title", "director", "released", "quantity"]

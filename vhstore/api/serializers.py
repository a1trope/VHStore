from rest_framework import serializers
from . import models


class CassetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cassette
        fields = "__all__"

from rest_framework import serializers
from .models import Cassette
from django.contrib.auth.models import User


class CassetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cassette
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

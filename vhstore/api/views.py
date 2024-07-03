from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers


@api_view(["GET"])
def get_cassettes(request):
    queryset = models.Cassette.objects.all()
    serializer = serializers.CassetteSerializer(queryset, many=True)

    return Response({"message": serializer.data})


@api_view(["POST"])
def create_cassette(request):
    return Response({"message": None})


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers


@api_view(["GET", "POST"])
def get_cassettes(request):
    if request.method == "GET":
        queryset = models.Cassette.objects.all()
        serializer = serializers.CassetteSerializer(queryset, many=True)

        return Response({"message": serializer.data})

    if request.method == "POST":
        serializer = serializers.CassetteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response({"message": serializer.errors}, status=400)

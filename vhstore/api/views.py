from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers


@api_view(["GET", "POST"])
def cassettes_list(request):
    if request.method == "GET":
        queryset = models.Cassette.objects.all()
        serializer = serializers.CassetteSerializer(queryset, many=True)

        return Response({"message": serializer.data})

    if request.method == "POST":
        serializer = serializers.CassetteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def cassettes_detail(request, id):
    if not models.Cassette.objects.filter(id=id).exists():
        return Response({"message": "Object doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)

    cassette = models.Cassette.objects.get(id=id)

    if request.method == "GET":
        serializer = serializers.CassetteSerializer(cassette)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = serializers.CassetteSerializer(cassette, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        cassette.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

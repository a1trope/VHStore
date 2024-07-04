from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def signup(request):
    serializer = serializers.UserSerializer(data=request.data)

    if serializer.is_valid():
        if User.objects.filter(username=request.data["username"]).exists():
            return Response({"message": f"User \"{request.data["username"]}\" already exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        user = User.objects.get(username=request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)

        return Response({"token": token.key, "user": serializer.data})

    return Response({"errors": serializer.errors})


@api_view(['POST'])
def login(request):
    serializer = serializers.UserSerializer(data=request.data)

    if serializer.is_valid():
        if not User.objects.filter(username=request.data["username"]).exists():
            return Response({"message": "User doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(username=request.data["username"])

        if not user.check_password(request.data["password"]):
            return Response({"message": f"Wrong password for \"{user.get_username()}\""}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key, "user": serializer.data})

    return Response({"errors": serializer.errors})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def signup(request):
    return Response()


@api_view(['POST'])
def login(request):
    if not User.objects.filter(username=request.data["username"]).exists():
        return Response({"message": "User doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.get(username=request.data["username"])
    serializer = serializers.UserSerializer(request.data)

    if not user.check_password(request.data["password"]):
        return Response({"message": f"Wrong password for \"{user.get_username()}\""}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)

    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def logout(request):
    return Response()

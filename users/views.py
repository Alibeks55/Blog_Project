from  rest_framework.response import Response
from rest_framework import  status, permissions
from rest_framework.views import APIView
from  . import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import UsersCod
from django.contrib.auth.models import User
import random


class RegistrationAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = serializers.UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(
        username=username,
        password=password,
        is_active=False
        )
        code = str(random.randint(100000, 999999))
        UsersCod.objects.create(user=user, code=code)

        return Response(
            data={'user_id': user.id,
              'confirmation_code': code},
            status=status.HTTP_201_CREATED
        )


class ConfirmAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        code = request.data.get('code')

        try:

            user = User.objects.get(username=username)
            user_code = UsersCod.objects.get(user=user)
        except (User.DoesNotExist, UsersCod.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if user_code.code == code:
           user.is_active = True
           user.save()
           return Response(data={'message': 'User confirmed'}, status=status.HTTP_200_OK)
        return Response(data={'error': 'invalid code'}, status=status.HTTP_400_BAD_REQUEST)


class AuthorizationAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = serializers.UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)

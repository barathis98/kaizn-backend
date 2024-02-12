from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from ..serializers import UserSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny
from ..models import Item

class NoAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return None 



class LoginView(APIView):
    authentication_classes = [NoAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        


class CreateUserView(APIView):
    authentication_classes = [NoAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
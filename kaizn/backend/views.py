from django.shortcuts import render

# Create your views here.
# views.py
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer, ItemSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import AllowAny
from .models import Item

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
            # User is authenticated, generate and return a token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Authentication failed
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
    
class ItemListView(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()

        # Filter items based on query parameters
        name = request.query_params.get('name', None)
        category = request.query_params.get('category', None)
        stock_status = request.query_params.get('stock_status', None)

        if name:
            items = items.filter(name__icontains=name)

        if category:
            items = items.filter(category__icontains=category)

        if stock_status == 'available':
            items = items.filter(stock_quantity__gt=0)
        elif stock_status == 'out_of_stock':
            items = items.filter(stock_quantity=0)

        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

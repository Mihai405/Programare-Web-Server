from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response

class RegisterView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
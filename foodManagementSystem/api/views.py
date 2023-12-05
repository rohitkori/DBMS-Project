from rest_framework.decorators import action  # Import this for the action decorator
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response  # Import this for Response
from rest_framework import status, viewsets  # Import this for Status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import *
from .serializers import MyTokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes, action

# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


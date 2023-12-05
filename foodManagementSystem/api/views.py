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
from .serializers import MyTokenObtainPairSerializer, UserSerializer, DonorSerializer, VolunteerSerializer, foodSerializer, pickup_requestSerializer, delivery_areaSerializer, distrubution_requestSerializer
from rest_framework.decorators import api_view, permission_classes, action


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class RegisterDonorViewSet(APIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = request.user
            user.isDonor = True
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterVolunteerViewSet(APIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = VolunteerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = request.user
            user.isVolunteer = True
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DonateFoodViewSet(APIView):
    queryset = food.objects.all()
    serializer_class = foodSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user = request.user
        donor = Donor.objects.get(user=user)

        if request.data.food_name:
            food_name = request.data.food_name
        if request.data.food_description:
            food_description = request.data.food_description
        
        food = food.objects.create(donator=donor, food_name=food_name, food_description=food_description)
        food.save()
        pickup_request = pickup_request.objects.create(food_id=food)

        return Response({"message": "Food Donated Successfully and Pickup-Request has been opened"}, status=status.HTTP_200_CREATED)
    
class OpenPickupRequestViewSet(APIView):
    queryset = pickup_request.objects.all()
    serializer_class = pickup_requestSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user = request.user
        volunteer = Volunteer.objects.get(user=user)
        open_pickup_requests = pickup_request.objects.filter(is_picked=False)
        return Response({"Requests": open_pickup_requests}, status=status.HTTP_200_OK)
    

class AcceptPickupRequestViewSet(APIView):
    queryset = pickup_request.objects.all()
    serializer_class = pickup_requestSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user = request.user
        volunteer = Volunteer.objects.get(user=user)
        pickup_request_id = request.data.pickup_request_id
        pickup_request = pickup_request.objects.get(id=pickup_request_id)
        pickup_request.pickup_person = volunteer
        pickup_request.save()

        return Response({"message": "Pickup Request Accepted"}, status=status.HTTP_200_OK) 
    
class PickUpDoneViewSet(APIView):
    queryset = pickup_request.objects.all()
    serializer_class = pickup_requestSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user = request.user
        volunteer = Volunteer.objects.get(user=user)
        pickup_request_id = request.data.pickup_request_id
        pickup_request = pickup_request.objects.get(id=pickup_request_id)
        pickup_request.is_picked = True
        pickup_request.save()

        return Response({"message": "Pickup Request Completed"}, status=status.HTTP_200_OK)
    

class DeliveryAreaViewSet(APIView):
    queryset = delivery_area.objects.all()
    serializer_class = delivery_areaSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user = request.user

        delivery_area_name = request.data.delivery_area_name
        delivery_area_description = request.data.delivery_area_description
        delivery_area_address = request.data.delivery_area_address
        delivery_area = delivery_area.objects.create(area_name=delivery_area_name, area_description=delivery_area_description, area_address=delivery_area_address)
        delivery_area.save()

        return Response({"message": "Delivery Area Created"}, status=status.HTTP_200_OK)
    
class OpenDistributionRequestViewSet(APIView):
    queryset = distrubution_request.objects.all()
    serializer_class = distrubution_requestSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):

        open_distribution_requests = distrubution_request.objects.filter(is_distributed=False)
        return Response({"Requests": open_distribution_requests}, status=status.HTTP_200_OK)

class AcceptDistributionRequestViewSet(APIView):
    queryset = distrubution_request.objects.all()
    serializer_class = distrubution_requestSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user = request.user
        volunteer = Volunteer.objects.get(user=user)
        distributed_by = volunteer
        distribution_area_id = request.data.distribution_area_id
        distribution_area = delivery_area.objects.get(id=distribution_area_id)
        is_distributed = False
        distribution_area.distributed_by = distributed_by
        distribution_area.save()

        return Response({"message": "Distribution Request Accepted"}, status=status.HTTP_200_OK)
    
class DistributionDoneViewSet(APIView):
    queryset = distrubution_request.objects.all()
    serializer_class = distrubution_requestSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        user = request.user
        volunteer = Volunteer.objects.get(user=user)
        distribution_request_id = request.data.distribution_request_id
        distribution_request = distrubution_request.objects.get(id=distribution_request_id)
        distribution_request.is_distributed = True
        distribution_request.save()

        return Response({"message": "Distribution Request Completed"}, status=status.HTTP_200_OK)
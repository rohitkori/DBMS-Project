from users.models import User, Donor, Volunteer, food, pickup_request, delivery_area, distrubution_request
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['isDonor'] = user.isDonor
        token['isVolunteer'] = user.isVolunteer


        return token

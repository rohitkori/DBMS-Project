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

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class foodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = '__all__'

class pickup_requestSerializer(serializers.ModelSerializer):

    class Meta:
        model = pickup_request
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(pickup_requestSerializer, self).to_representation(instance)
        rep['pickup_address'] = instance.food_id.donator.donor_address
        return rep


class delivery_areaSerializer(serializers.ModelSerializer):

    class Meta:
        model = delivery_area
        fields = '__all__'

class distrubution_requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = distrubution_request
        fields = '__all__'
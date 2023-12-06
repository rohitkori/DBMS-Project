from rest_framework.routers import DefaultRouter
from rest_framework import routers
from django.urls import path, include
from .views import MyTokenObtainPairView, UserViewSet, RegisterDonorViewSet, RegisterVolunteerViewSet
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/donor/', RegisterDonorViewSet.as_view(), name='register_donor'),
    path('register/volunteer/', RegisterVolunteerViewSet.as_view(), name='register_volunteer'),
    path('donate/', DonateFoodViewSet.as_view(), name='donate_food'),
    path('open-pickups/', OpenPickupRequestViewSet.as_view(), name='pickup_request'),
    path('accept-pickup/', AcceptPickupRequestViewSet.as_view(), name='accept_pickup'),
    path('done-pickup/', PickUpDoneViewSet.as_view(), name='done_pickup'),
    path('delivery-area/', DeliveryAreaViewSet.as_view(), name='delivery_area'),
    path('open-distributions/', OpenDistributionRequestViewSet.as_view(), name='open_distribution'),
    path('accept-distribution/', AcceptDistributionRequestViewSet.as_view(), name='accept_distribution'),
    path('done-distribution/', DistributionDoneViewSet.as_view(), name='done_distribution'),
    path('pickup-accept/', PickupAcceptViewSet.as_view(), name='pickup_accept'),
]
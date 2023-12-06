from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('NotSay', 'NotSay'),
    ('Other', 'Other'),
)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, null=False)
    USERNAME_FIELD = 'email'
    isDonor = models.BooleanField(default=False)
    isVolunteer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
    
class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default="Donor ID")
    donor_name = models.CharField(max_length=250, null=False, blank=False, default="Donor Name")
    donor_contact = models.CharField(max_length=250, null=False, blank=False, default="Donor Contact")
    donor_address = models.CharField(max_length=250, null=False, blank=False, default="Donor Address")
    
    def __str__(self):
        return self.donor_name


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default="Volunteer ID")
    volunteer_name = models.CharField(max_length=250, null=False, blank=False, default="Volunteer Name")
    volunteer_contact = models.CharField(max_length=250, null=False, blank=False, default="Volunteer Contact")
    volunteer_address = models.CharField(max_length=250, null=False, blank=False, default="Volunteer Address")

    def __str__(self):
        return self.user.id

class food(models.Model):
    donator = models.ForeignKey(Donor, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=250, null=True, blank=True, default="Food Name")
    food_description = models.CharField(max_length=250, null=True, blank=True,  default="Food Description")

    def __str__(self):
        return self.food_name
    
class pickup_request(models.Model):
    pickup_person = models.ForeignKey(Volunteer, on_delete=models.CASCADE, blank=True, null=True)
    food_id = models.OneToOneField(food, on_delete=models.CASCADE)
    is_picked = models.BooleanField(default=False)

    def __str__(self):
        return self.food_id.food_name 
    
class delivery_area(models.Model):
    area_name = models.CharField(max_length=250, null=False, blank=False, default="Area")
    area_description = models.CharField(max_length=250, null=True, blank=True, default="Area Description")
    area_address = models.CharField(max_length=250, null=False, blank=False, default="Area Address")

    def __str__(self):
        return self.area_name

class distrubution_request(models.Model):
    # food_id = models.OneToOneField(food, on_delete=models.CASCADE)
    distributed_by = models.ForeignKey(Volunteer, on_delete=models.CASCADE, blank=True, null=True)
    distribution_area = models.ForeignKey(delivery_area, on_delete=models.CASCADE)
    is_distributed = models.BooleanField(default=False)

    def __str__(self):
        return self.distribution_area.area_name



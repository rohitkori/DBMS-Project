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
    username = models.CharField(max_length=250, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    USERNAME_FIELD = 'email'
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
    
class Donor(models.Model):
    donor_id = models.CharField(max_length=250, null=False, blank=False, primary_key=True, default="Donor ID")
    # id = models.CharField(max_length=250, null=False, blank=False, primary_key=True, default="Donor ID")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    donor_name = models.CharField(max_length=250, null=False, blank=False, default="Donor Name")
    donor_contact = models.CharField(max_length=250, null=False, blank=False, default="Donor Contact")
    donor_address = models.CharField(max_length=250, null=False, blank=False, default="Donor Address")
    
    def __str__(self):
        return self.donor_id


class Volunteer(models.Model):
    volounteer_id = models.CharField(max_length=250, null=False, blank=False, primary_key=True, default="Volunteer ID")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    volunteer_name = models.CharField(max_length=250, null=False, blank=False, default="Volunteer Name")
    volunteer_contact = models.CharField(max_length=250, null=False, blank=False, default="Volunteer Contact")
    volunteer_address = models.CharField(max_length=250, null=False, blank=False, default="Volunteer Address")

    def __str__(self):
        return self.volunteer_id

class food(models.Model):
    food_id = models.CharField(max_length=250, null=False, blank=False, primary_key=True, default="Food ID")
    donator = models.ForeignKey(Donor, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=250, null=True, blank=True, default="Food Name")
    food_description = models.CharField(max_length=250, null=True, blank=True,  default="Food Description")

    def __str__(self):
        return self.food_id
    
class pickup_request(models.Model):
    pick_id = models.CharField(max_length=250, null=False, blank=False, primary_key=True, default="Pickup ID")
    pickup_person = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    food_id = models.OneToOneField(food, on_delete=models.CASCADE)
    is_picked = models.BooleanField(default=False)

    def __str__(self):
        return self.pick_id
    
class delivery_area(models.Model):
    area_id = models.CharField(max_length=250, null=False, blank=False, primary_key=True, default="Area ID")
    area_name = models.CharField(max_length=250, null=False, blank=False, default="Area")
    area_description = models.CharField(max_length=250, null=True, blank=True, default="Area Description")
    area_address = models.CharField(max_length=250, null=False, blank=False, default="Area Address")

    def __str__(self):
        return self.area_id

class distrubution_request(models.Model):
    dist_id = models.CharField(max_length=250, null=False, blank=False, primary_key=True, default="Distribution ID")
    food_id = models.OneToOneField(food, on_delete=models.CASCADE)
    distributed_by = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    distribution_area = models.ForeignKey(delivery_area, on_delete=models.CASCADE)
    is_distributed = models.BooleanField(default=False)

    def __str__(self):
        return self.dist_id



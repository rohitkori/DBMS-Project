from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from .models import User, Donor, Volunteer, food, pickup_request, delivery_area, distrubution_request

# Register your models here.


@admin.register(User)
class UserAdmin(ImportExportModelAdmin, DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'isDonor', 'isVolunteer', 'first_name', 'last_name')}),
        # (_('Personal info'), {'fields': ('first_name', 'last_name', 'gender', 'contact')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    list_display = ( 'email',)
    # list_filter = ('isFreelancer', 'isRecruiter', 'course_enrolled', 'current_year')
    # search_fields = ['username', 'email', 'first_name', 'last_name',]
    ordering = ('email',)

    class Meta:
        model = User
        fields = '__all__'

@admin.register(Donor)
class DonorAdmin(ImportExportModelAdmin):
    list_display = ('user', 'donor_name', 'donor_contact', 'donor_address')
    ordering = ('user__id',)

    class Meta:
        model = Donor
        fields = '__all__'

@admin.register(Volunteer)

class VolunteerAdmin(ImportExportModelAdmin):
    list_display = ( 'user', 'volunteer_name', 'volunteer_contact', 'volunteer_address')
    ordering = ('user__id',)

    class Meta:
        model = Volunteer
        fields = '__all__'

@admin.register(food)
class foodAdmin(ImportExportModelAdmin):
    list_display = ('id', 'donator', 'food_name', 'food_description')
    ordering = ('id',)

    class Meta:
        model = food
        fields = '__all__'

@admin.register(pickup_request)

class pickup_requestAdmin(ImportExportModelAdmin):
    list_display = ('id', 'pickup_person', 'food_id', 'is_picked')
    ordering = ('id',)

    class Meta:
        model = pickup_request
        fields = '__all__'

@admin.register(delivery_area)
class delivery_areaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'area_name', 'area_description', 'area_address')
    ordering = ('id',)

    class Meta:
        model = delivery_area
        fields = '__all__'
    

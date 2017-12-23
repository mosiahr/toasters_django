from django.contrib import admin
from profiles.models import Profile, Location, Tag

from django.contrib.auth import get_user_model
User = get_user_model()


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile

    list_display = ('user', 'name', )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    class Meta:
        model = Location

    list_display = ('name', 'slug')
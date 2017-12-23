from django.contrib import admin
from .models import TypeCompany, Location, Tag, Company

from django.contrib.auth import get_user_model
User = get_user_model()


@admin.register(TypeCompany)
class TypeCompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = TypeCompany


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Location


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Tag


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    class Meta:
        model = Company
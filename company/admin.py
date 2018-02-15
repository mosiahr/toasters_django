from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext as _, ugettext_lazy

from .models import TypeCompany, Location, Company, Price

from django.contrib.auth import get_user_model
User = get_user_model()


@admin.register(TypeCompany)
class TypeCompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ['name']

    class Meta:
        model = TypeCompany


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Location


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    ordering = ['id']

    class Meta:
        model = Price


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'get_types', 'get_locations', 'created']
    # readonly_fields = ('user',)
    fields = ('name', 'type', 'address', 'email',
              'phone', 'site', 'description', 'img', 'locations', 'tags', 'price')

    actions = ['delete_selected']

    class Meta:
        model = Company

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(CompanyAdmin, self).save_model(request, obj, form, change)

    def delete_selected(self, request, queryset):
        if not self.has_delete_permission(request):
            raise PermissionDenied
        for obj in queryset:
            obj.delete()

    delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")

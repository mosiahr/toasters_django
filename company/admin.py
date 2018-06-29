from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext as _, ugettext_lazy

from easy_select2 import select2_modelform

from .models import TypeCompany, Location, Company, Price
from gallery.models import Album, Photo

from .forms import CompanyAddForm

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


# @admin.register(Photo)
# class PriceAdmin(admin.ModelAdmin):
#     list_display = ['name', 'image']
#     # ordering = ['id']
#
#     class Meta:
#         model = Photo
#
#

class PhotoInline(admin.TabularInline):
    model = Photo
    # fields = ('name', 'title', 'image', 'album')
    # min_num = 0
    extra = 0


CompanyForm = select2_modelform(Company, attrs={'width': '250px'})


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    # form = CompanyAddForm
    list_display = ['name', 'publish', 'user', 'type', 'get_locations', 'created']
    list_filter = ('user', 'type', 'location', 'price')
    # readonly_fields = ('user',)
    fields = ('name', 'type', 'address', 'email',
              'phone', 'site', 'description', 'avatar',
              # 'album',
              'location', 'tags', 'price', 'publish')

    actions = ['delete_selected']
    list_editable = ('publish',)  # edit

    # inlines = [
    #     PhotoInline,
    # ]

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

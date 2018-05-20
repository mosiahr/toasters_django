from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import Photo, Album

from django.utils.translation import ugettext as _, ugettext_lazy

from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline


class PhotoInline(admin.TabularInline):
    model = Photo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ('name', 'summary')

    inlines = [
        PhotoInline,
    ]

    actions = ['delete_selected']

    class Meta:
        model = Album

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(AlbumAdmin, self).save_model(request, obj, form, change)

    def delete_selected(self, request, queryset):
        if not self.has_delete_permission(request):
            raise PermissionDenied
        for obj in queryset:
            # print(obj)
            obj.delete()

    delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'album']
    actions = ['delete_selected']

    class Meta:
        model = Photo

    def delete_selected(self, request, queryset):
        if not self.has_delete_permission(request):
            raise PermissionDenied
        for obj in queryset:
            obj.delete()

    delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")


from django.contrib import admin
from django.core.exceptions import PermissionDenied
from .models import Photo, Album

from django.utils.translation import ugettext as _, ugettext_lazy

from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline


class PhotoInline(admin.TabularInline):
    model = Photo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'cover_photo', 'company', 'get_count_photo']
    fields = ('name', 'summary', 'company')
    list_filter = ('company',)

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

    def cover_photo(self, obj):
        cover_photo = obj.get_cover_photo()
        img = None
        if cover_photo:
            img = Photo.objects.get(id=cover_photo.id).image.small.url
        return '<img src="%s" title="%s" />' % (img, obj.name)
    cover_photo.allow_tags = True
    cover_photo.short_description = _("Cover photo")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['small_photo', 'name', 'image', 'album', 'image_thumbnail', 'image_thumbnail_size']
    actions = ['delete_selected']

    class Meta:
        model = Photo

    def delete_selected(self, request, queryset):
        if not self.has_delete_permission(request):
            raise PermissionDenied
        for obj in queryset:
            obj.delete()
    delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")

    def small_photo(self, obj):
        photo = obj.image.small.url
        return '<img src="%s" title="%s" />' % (photo, obj.name)
    small_photo.allow_tags = True

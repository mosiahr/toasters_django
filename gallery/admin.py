from django.contrib import admin

from .models import Photo, Album

from django.utils.translation import ugettext as _, ugettext_lazy

from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline


# class PhotoInline(admin.TabularInline):
#     model = Photo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug']
    # inlines = [
    #     PhotoInline,
    # ]

    class Meta:
        model = Album


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'image', 'album']

    class Meta:
        model = Photo

    def delete_selected(self, request, queryset):
        # if not self.has_delete_permission(request):
        #     raise PermissionDenied
        for obj in queryset:
            obj.delete()

    delete_selected.short_description = ugettext_lazy("Delete selected %(verbose_name_plural)s")


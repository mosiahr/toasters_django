from django.contrib import admin

from .models import (
    Toaster,
    Location,
    Tag,
)


class ToasterAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Toaster._meta.fields if field.name != 'id' and field.name != 'description' ]
    list_display = ['name', 'get_locations', 'publish']
    list_filter = ['name']

    class Meta:
        model = Toaster


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Tag


class ToasterLocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Location


admin.site.register(Toaster, ToasterAdmin)
admin.site.register(Location, ToasterLocationAdmin)
admin.site.register(Tag, TagAdmin)

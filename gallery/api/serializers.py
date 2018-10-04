from rest_framework import serializers
from django.contrib.sessions.models import Session

# from django.contrib.auth.models import User
# from django.contrib.auth.validators import UnicodeUsernameValidator

from gallery.models import Album, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        # fields = ('image_thumbnail',)
        fields = ('id', 'name', 'album', 'is_cover_photo', 'image', 'image_thumbnail', 'image_thumbnail_size')


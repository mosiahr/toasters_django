from rest_framework import serializers
from django.contrib.sessions.models import Session

# from django.contrib.auth.models import User
# from django.contrib.auth.validators import UnicodeUsernameValidator

from gallery.models import Album, Photo
from accounts.api.serializers import UserSerializer


class AlbumSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Album
        fields = ('id', 'name', 'author', 'summary', 'company')


class PhotoSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    album = AlbumSerializer()

    class Meta:
        model = Photo
        fields = ('id', 'name', 'author', 'album', 'is_cover_photo', 'image', 'image_thumbnail', 'image_thumbnail_size')


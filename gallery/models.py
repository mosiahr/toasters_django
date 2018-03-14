from django.db import models

from django.utils.translation import ugettext as _

from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID


class Album(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    summary = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_cover_photo(self):
        if self.photo_set.filter(is_cover_photo=True).count() > 0:
            return self.photo_set.filter(is_cover_photo=True)[0]
        elif self.photo_set.all().count() > 0:
            return self.photo_set.all()[0]
        else:
            return None


DEFAULT_ID = 1


class Photo(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='photos/%Y/%m')
    image = StdImageField(upload_to=UploadToUUID(path='photos'),
                           variations={
                               # 'medium': (300, 300),
                               'thumbnail': {'width': 200, 'height': 200, "crop": True}
                           })

    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=DEFAULT_ID)
    is_cover_photo = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_cover_photo:
            other_cover_photo = Photo.objects.filter(album=self.album).filter(is_cover_photo=True)
            for photo in other_cover_photo:
                photo.is_cover_photo = False
                photo.save()
        super(Photo, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Photo, self).delete(*args, **kwargs)





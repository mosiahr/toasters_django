from django.db import models
from django.utils.translation import ugettext as _

from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID

from company.models import Company

from django.contrib.auth import get_user_model
User = get_user_model()


# class CompanyManager(models.Manager):
#     """ Set Filter """
#     def get_queryset(self):
#         return super(CompanyManager, self).get_queryset().filter(album_id=self.id)

def set_default_name(pk, name=_('Portfolio')):
    if Photo.objects.filter(album_id=pk).count() > 1:
        return ''
    return name


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, verbose_name=_('Name'))
    # slug = models.SlugField()
    summary = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    # objects = CompanyManager()

    class Meta:
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')

    def __str__(self):
        return self.name

    def get_cover_photo(self):
        if self.photo_set.filter(is_cover_photo=True).exists():
            return self.photo_set.filter(is_cover_photo=True)[0]
        elif self.photo_set.all().exists():
            return self.photo_set.all()[0]
        else:
            return None

    def get_photo(self):
        if self.photo_set.filter(album_id=self.id).exists():
            return self.photo_set.filter(album_id=self.id)

    def get_count_photo(self):
        photos = self.get_photo()
        return photos.count()

    def delete(self, *args, **kwargs):
        for photo in self.photo_set.all():
            Photo.objects.get(id=photo.id).delete(*args, **kwargs)
        super(Album, self).delete(*args, **kwargs)


class Photo(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Name'))
    title = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Title'))
    # image = models.ImageField(upload_to='photos/%Y/%m')
    image = StdImageField(upload_to=UploadToUUID(path='photos'),
                          variations={
                              # 'medium': (300, 300),
                              'thumbnail': {'width': 200, 'height': 200, "crop": True}
                          },
                          verbose_name=_('Image'))

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    is_cover_photo = models.BooleanField(verbose_name=_('Is cover photo '))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')

    def __str__(self):
        return 'ID: {}'.format(self.id)

    def save(self, *args, **kwargs):
        if self.is_cover_photo:
            other_cover_photo = Photo.objects.filter(album=self.album).filter(is_cover_photo=True)
            for photo in other_cover_photo:
                photo.is_cover_photo = False
                photo.save()
        try:
            this_record = Photo.objects.get(id=self.id)
            if this_record.image != self.image:
                this_record.image.delete(save=False)
        except:
            pass
        super(Photo, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(Photo, self).delete(*args, **kwargs)

from django.db import models
from django.utils.translation import ugettext as _

from stdimage.models import StdImageField
from PIL import Image
from stdimage.utils import UploadToUUID

from company.models import Company
from core.models_abstract import MainAbstractModel

from django.db.models.signals import post_save

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


class UserManager(models.Manager):
    """ Set Filter only current user """
    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(user=self.request.user)


class Album(MainAbstractModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # save into form.py and save_model into admin.py
    name = models.CharField(max_length=70, verbose_name=_('Name'), default=_('Portfolio'))
    # slug = models.SlugField()
    summary = models.TextField(blank=True, null=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_("Company"))

    # objects = UserManager()

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
        try:
            photos = self.get_photo()
            return photos.count()
        except:
            return 0

    def is_album_empty(self):
        if self.get_count_photo() > 0:
            return False
        else:
            return True

    get_count_photo.short_description = _("Count")
    
    def delete(self, *args, **kwargs):
        for photo in self.photo_set.all():
            Photo.objects.get(id=photo.id).delete(*args, **kwargs)
        super(Album, self).delete(*args, **kwargs)


class Photo(MainAbstractModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # save into form.py and save_model into admin.py
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Name'))
    # title = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Title'))
    # image = models.ImageField(upload_to=UploadToUUID(path='photo'))

    image = StdImageField(upload_to=UploadToUUID(path='photos'),
                          variations={
                              # 'medium': (300, 300),
                              'thumbnail': (320, 320),
                              'small': {'width': 100, 'height': 100, "crop": True}
                          },
                          verbose_name=_('Image'))

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    is_cover_photo = models.BooleanField(verbose_name=_('Is cover photo '))
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')

    def __str__(self):
        return 'Photo with ID: %s' % self.id

    @property
    def image_thumbnail(self):
        return self.image.thumbnail.url

    @property
    def image_thumbnail_size(self):
        try:
            width, height = Image.open(self.image.thumbnail).size
        except:
            width = height = None
        return width, height

    def small_photo(self):
        photo = self.image.small.url
        return '<img src="%s" title="%s" />' % (photo, self.name)

    def save(self, request=False, *args, **kwargs):
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

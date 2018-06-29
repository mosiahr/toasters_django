from django.db import models

from stdimage.models import StdImageField
from stdimage.utils import (UploadToUUID, UploadToClassNameDir,
                            UploadToAutoSlug, UploadToAutoSlugClassNameDir)

from django.shortcuts import reverse
from django.utils.translation import ugettext as _
from core.models_abstract import MainAbstractModel

from tags.models import Tag

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth import get_user_model
User = get_user_model()


class Location(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name=_('City'))
    slug = models.SlugField(max_length=140, blank=True, null=True)

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')
        ordering = ['name']


class TypeCompany(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name=_('Company type'))
    slug = models.SlugField(max_length=140, blank=True, null=True)

    class Meta:
        verbose_name = _('Company type')
        verbose_name_plural = _('Company types')
        ordering = ['name']


class Price(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name=_('Price'))
    slug = models.SlugField(max_length=140, blank=True, null=True)

    class Meta:
        verbose_name = _('Price')
        verbose_name_plural = _('Prices')


# class Photo(MainAbstractModel):
#     name = models.CharField(max_length=120, verbose_name=_('Photo'))
#     image = StdImageField(upload_to=UploadToUUID(path='images'),  # 'img',
#                            variations={
#                                'medium': (300, 300),
#                                'thumbnail': {'width': 200, 'height': 200, "crop": True}
#                            },
#                            verbose_name=_('Image'))

# from gallery.models import Album


class Company(MainAbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=140, unique=False, verbose_name=_('Name'))
    type = models.ForeignKey(TypeCompany, verbose_name=_('Type'))
    address = models.CharField(max_length=140, verbose_name=_('Address'), blank=True)
    email = models.EmailField(blank=True, verbose_name=_('email'))
    phone = models.CharField(max_length=50, verbose_name=_('Phone'), blank=True)
    site = models.CharField(max_length=50, verbose_name=_('Site'), blank=True)
    # description = models.TextField(max_length=1000, verbose_name=_('Description'), blank=True)
    description = RichTextField(verbose_name=_('Description'), blank=True)

    # avatar = models.ImageField(upload_to='img', verbose_name=_('Logo'))  #upload_to='img/%Y/%m/%d
    avatar = StdImageField(upload_to=UploadToUUID(path='images'),  #'img',
                           variations={
                               'medium': (300, 300),
                               'thumbnail': {'width': 200, 'height': 200, "crop": True},
                               'small': {'width': 100, 'height': 100, "crop": True}
                           },
                           verbose_name=_('Logo'))

    location = models.ManyToManyField(Location, verbose_name=_('City'), blank=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), blank=True)
    price = models.ForeignKey(Price, verbose_name=_('Price'), on_delete=models.CASCADE)

    def get_locations(self):
        return ", \n".join([l.name for l in self.location.all()])

    # def get_types(self):
    #     return ", \n".join([t.name for t in self.type.all()])

    def get_absolute_url(self):
        return reverse('company:company_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        try:
            this_record = Company.objects.get(id=self.id)
            if this_record.avatar != self.avatar:
                this_record.avatar.delete(save=False)
        except:
            pass

        super(Company, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.avatar.delete(save=False)
        super(Company, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

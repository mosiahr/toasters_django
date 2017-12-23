from django.db import models
from django.utils.translation import ugettext as _

from core.models_abstract import MainAbstractModel

from django.contrib.auth import get_user_model
User = get_user_model()


class Tag(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name=_('Tag name'))
    slug = models.SlugField(max_length=140, blank=True, null=True)


class Location(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name=_('City'))
    slug = models.SlugField(max_length=140, blank=True, null=True)


class TypeCompany(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name=_('Type company'))
    slug = models.SlugField(max_length=140, blank=True, null=True)

    class Meta:
        verbose_name = _('Type company')
        verbose_name_plural = _('Type companies')


class Company(MainAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=140, unique=False, verbose_name=_('Name'), blank=True)
    type = models.ManyToManyField(TypeCompany, verbose_name=_('Type'), blank=True)
    address = models.CharField(max_length=140, verbose_name=_('Address'), blank=True)
    email = models.CharField(max_length=50, blank=True, verbose_name=_('email'))
    phone = models.CharField(max_length=50, verbose_name=_('Phone'), blank=True)
    site = models.CharField(max_length=50, verbose_name=_('Site'), blank=True)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    img = models.ImageField(upload_to='img', verbose_name=_('Logo'), blank=True)
    locations = models.ManyToManyField(Location, verbose_name=_('City'), blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def get_locations(self):
        return "\n".join([l.name for l in self.locations.all()])

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


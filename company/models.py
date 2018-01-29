from django.db import models
from django.shortcuts import reverse
from django.utils.translation import ugettext as _
from core.models_abstract import MainAbstractModel

from django.contrib.auth import get_user_model
User = get_user_model()


class Tag(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name=_('Tag name'))
    slug = models.SlugField(max_length=140, blank=True, null=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


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


def get_user(request=None):
    try:
        return User.objects.get(request.user)
    except:
        pass


class Company(MainAbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_user)
    name = models.CharField(max_length=140, unique=False, verbose_name=_('Name'))
    type = models.ManyToManyField(TypeCompany, verbose_name=_('Type'))
    address = models.CharField(max_length=140, verbose_name=_('Address'), blank=True)
    email = models.EmailField(blank=True, verbose_name=_('email'))
    phone = models.CharField(max_length=50, verbose_name=_('Phone'), blank=True)
    site = models.CharField(max_length=50, verbose_name=_('Site'), blank=True)
    description = models.TextField(max_length=350, verbose_name=_('Description'), blank=True)
    img = models.ImageField(upload_to='img', verbose_name=_('Logo'))
    locations = models.ManyToManyField(Location, verbose_name=_('City'), blank=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), blank=True)
    price = models.ForeignKey(Price, verbose_name=_('Price'), on_delete=models.CASCADE)

    def get_locations(self):
        return ", \n".join([l.name for l in self.locations.all()])

    def get_absolute_url(self):
        return reverse('company:company_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        try:
            this_record = Company.objects.get(pk=self.user_id)
            if this_record.img != self.img:
                this_record.img.delete(save=False)
        except:
            pass
        super(Company, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.img.delete(save=False)
        super(Company, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

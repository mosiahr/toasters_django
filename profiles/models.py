from django.db import models

from core.models_abstract import MainAbstractModel

from django.contrib.auth import get_user_model
User = get_user_model()


class Tag(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name='Имя тега')
    slug = models.SlugField(max_length=140, blank=True, null=True)


class Location(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name='Город')
    slug = models.SlugField(max_length=140, blank=True, null=True)


class Profile(MainAbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=140, unique=False, verbose_name='Имя', blank=True)
    address = models.CharField(max_length=140, verbose_name='Адрес', blank=True)
    email = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, verbose_name='Телефон', blank=True)
    site = models.CharField(max_length=50, verbose_name='Сайт', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    img = models.ImageField(upload_to='img', verbose_name='Картинка', blank=True)
    locations = models.ManyToManyField(Location, verbose_name='Город', blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def get_locations(self):
        return "\n".join([l.name for l in self.locations.all()])





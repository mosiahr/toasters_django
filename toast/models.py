from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()


class PublishManager(models.Manager):
    """ Set Filter publish=True """
    def get_queryset(self, publ=True):
        return super(PublishManager, self).get_queryset().filter(publish=publ)


class MainAbstractModel(models.Model):
    name = None
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True, db_index=True, verbose_name="Публикация")
    objects = models.Manager()  # default
    pub_objects = PublishManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<{} id: {}, Name: {}>'.format(self.__class__.__name__, self.id, self.name)


class Tag(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name='Имя тега')
    slug = models.SlugField(max_length=140, blank=True, null=True)


class Location(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name='Город')
    slug = models.SlugField(max_length=140, blank=True, null=True)


class Toaster(MainAbstractModel):
    name = models.CharField(max_length=140, unique=True, verbose_name='Имя')
    address = models.CharField(max_length=140, verbose_name='Адрес')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    site = models.CharField(max_length=50, verbose_name='Сайт')
    description = models.TextField(blank=True, verbose_name='Описание')
    img = models.ImageField(upload_to='img', verbose_name='Картинка')
    locations = models.ManyToManyField(Location, verbose_name='Город')
    tags = models.ManyToManyField(Tag)

    def get_locations(self):
        return "\n".join([l.name for l in self.locations.all()])


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
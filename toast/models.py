from django.db import models


class PublishManager(models.Manager):
    """ Set Filter publish=True """
    def get_queryset(self, publ=True):
        return super(PublishManager, self).get_queryset().filter(publish=publ)


class ToastAbstractModel(models.Model):
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


class Tag(ToastAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name='Имя тега')
    slug = models.SlugField(max_length=140, blank=True, null=True)


class ToasterLocation(ToastAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name='Город')
    slug = models.SlugField(max_length=140, blank=True, null=True)


class Toaster(ToastAbstractModel):
    name = models.CharField(max_length=140, unique=True, verbose_name='Имя')
    address = models.CharField(max_length=140, verbose_name='Адрес')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    site = models.CharField(max_length=50, verbose_name='Сайт')
    description = models.TextField(blank=True, verbose_name='Описание')
    img = models.ImageField(upload_to='img', verbose_name='Картинка')
    locations = models.ManyToManyField(ToasterLocation, verbose_name='Город')
    tags = models.ManyToManyField(Tag)

    def get_locations(self):
        return "\n".join([l.name for l in self.locations.all()])


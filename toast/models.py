from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Имя тега')
    slug = models.SlugField(max_length=140, blank=True, null=True)

    def __repr__(self):
        return '<Tag id: {}, Name: {}>'.format(self.id, self.name)

    def __str__(self):
        return self.name


class Toaster(models.Model):
    name = models.CharField(max_length=140, unique=True, verbose_name='Имя')
    address = models.CharField(max_length=140, verbose_name='Адрес')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    site = models.CharField(max_length=50, verbose_name='Сайт')
    description = models.TextField(blank=True, verbose_name='Описание')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Toaster id: {}, Name: {}>'.format(self.id, self.name)




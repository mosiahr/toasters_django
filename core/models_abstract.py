from django.db import models

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
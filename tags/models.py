from django.db import models
from django.utils.translation import ugettext as _

from core.models_abstract import MainAbstractModel


class Tag(MainAbstractModel):
    name = models.CharField(max_length=120, unique=True, verbose_name=_('Tag name'))
    slug = models.SlugField(max_length=140, blank=True, null=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

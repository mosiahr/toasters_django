from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TagsConfig(AppConfig):
    name = 'tags'
    verbose_name = _('Tags')


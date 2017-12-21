from django.dispatch import Signal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import get_template

User = get_user_model()


@receiver(post_save, sender=User)
def user_save_handler(sender, instance, created, *args, **kwargs):
    if created:
        if settings.DEBUG:
            print("%s saved." % instance)
        obj = User.objects.get(pk=instance.id)
        if obj.is_active is not True:
            obj.send_activate()


@receiver(post_delete, sender=User)
def user_delete_handler(sender, **kwargs):
    if settings.DEBUG:
        print("%s deleted." % kwargs['instance'])



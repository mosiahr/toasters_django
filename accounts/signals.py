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
        print(obj, instance.id)
        obj.send_activate()

@receiver(post_delete, sender=User)
def user_delete_handler(sender, **kwargs):
    if settings.DEBUG:
        print("%s deleted." % kwargs['instance'])

def send_activate(email):
    base_url = getattr(settings, 'BASE_URL')
    print(base_url)
    #key_path = reverse("account:email-activate", kwargs={'key': self.key}) # use reverse
    key_path = None
    path = "{base}{path}".format(base=base_url, path=key_path)
    context = {
        'email': email,
        'path': path,
    }
    print(settings.EMAIL_HOST_USER)
    print(email)
    send_email = send_mail(
        subject='Activate your account at toasters.com.',
        message=get_template('accounts/email/verify.txt').render(context),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        html_message=get_template('accounts/email/verify.html').render(context),
        fail_silently=False,
    )
    return send_email




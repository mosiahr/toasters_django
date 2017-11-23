from django.db import models
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(
            email=self.normalize_email(email),
        )
        user_obj.set_password(password)  # change user password
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)  #superuser
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'  # used as the unique identifier.
    REQUIRED_FIELDS = [] # ['full_name'] #python manage.py createsuperuser

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        permissions = set()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    #@property
    #def is_active(self):
    #    return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.admin


    def send_activate(self):
        print('hii', self.email)
        base_url = getattr(settings, 'BASE_URL')
        #key_path = reverse("account:email-activate", kwargs={'key': self.key}) # use reverse
        key_path = reverse('accounts:activate', kwargs={'uid': self.id})
        path = "{base}{path}".format(base=base_url, path=key_path)
        context = {
            'email': self.email,
            'path': path,
        }
        #send_email = send_mail(
        #    subject='Activate your account at toasters.com.',
        #    message=get_template('accounts/email/verify.txt').render(context),
        #    from_email=settings.EMAIL_HOST_USER,
        #    recipient_list=[self.email],
        #    html_message=get_template('accounts/email/verify.html').render(context),
        #    fail_silently=False,
        #)

        #message_html = get_template('accounts/email/verify.html').render(context)
        message_txt = get_template('accounts/email/verify.txt').render(context)

        email = EmailMessage(
            subject='Activate your account at toasters.com.',
            body=message_txt,
            from_email=settings.EMAIL_HOST_USER,
            to=[self.email],
        )
        #email.attach_alternative(message_html, "text/html")
        #email.content_subtype = 'html'


        return email.send(fail_silently=False)


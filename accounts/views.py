from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views
from django.contrib import auth
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
    UserChangeForm,
)


from django.views.generic import FormView, CreateView, DetailView, View
from django.views.generic.edit import FormMixin

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import (
    MyAuthenticationForm,
    # MyPasswordChangeForm,
    # RegisterForm,
    # UpdateUserForm,
    # AddFieldToRegister

    LoginForm,
    RegisterForm,
)
from django.utils.translation import ugettext as _


from .tokens import account_activation_token

# from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()


from toast.views import ToasterListView

class AccountHomeView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/home.html'

    def get_object(self):
        return self.request.user

class AccountActivateView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')

class LoginView(FormView):
    form_class = LoginForm
    success_url = '/accounts/'
    template_name = 'accounts/login.html'
    default_next = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['title'] = _('Register')
        return context

class AppLogoutView(views.LogoutView):
    next_page = '/accounts/login/'

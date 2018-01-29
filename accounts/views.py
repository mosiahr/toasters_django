from django.shortcuts import render,  redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm

from django.views.generic import FormView, CreateView, DetailView, View, UpdateView
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import (
    LoginForm,
    RegisterForm,
    UserDetailChangeForm,
)
from django.utils.translation import ugettext as _

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import update_session_auth_hash

from .tokens import account_activation_token
from .messages import ErrorMessageMixin

from company.models import Company

from django.contrib.auth import get_user_model

User = get_user_model()


class AccountHomeView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/home.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(AccountHomeView, self).get_context_data(**kwargs)
        try:
            context['companies'] = Company.objects.filter(user_id=self.get_object())
        except:
            context['companies'] = None
        context['title'] = _('Account')
        return context


class AccountActivateView(View):
    template_name = 'accounts/activate_done.html'

    def get(self, request, uidb64, token, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()

            msg = _('Thank you for your email confirmation. Now you can login your account.')
        else:
            msg = _('Activation link is invalid!')

        context = {
            'title': _('Email confirmation'),
            'msg': msg
        }
        return render(request, self.template_name, context)


class LoginView(SuccessMessageMixin,
                ErrorMessageMixin,
                FormView):

    form_class = LoginForm
    success_url = '/accounts/'
    template_name = 'accounts/login.html'
    default_next = '/'
    success_message = _("Login successful!")
    error_message = _('Please correct the errors below.')

    def get_form_kwargs(self):
        kwargs = super(LoginView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get(self, request, *args, **kwargs):
        # if the user is authorized, then redirect to the success url
        if auth.get_user(request).is_authenticated:
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data())


class RegisterView(SuccessMessageMixin, ErrorMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/accounts/register/done/'
    success_message = _("Account %(email)s was created successfully!")
    error_message = _('Please correct the errors below.')

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['title'] = _('Register')
        return context


class DoneRegisterView(View):
    template_name = 'accounts/register_done.html'

    def get(self, request, **kwargs):
        msg = _("Please confirm your email address  to complete the registration.")

        context = {
            'title': _("Register is done"),
            'msg': msg
        }
        return render(request, self.template_name, context)


class AppLogoutView(views.LogoutView):
    next_page = '/accounts/login/'


class UserDetailUpdateView(LoginRequiredMixin,
                           SuccessMessageMixin,
                           ErrorMessageMixin,
                           UpdateView):

    form_class = UserDetailChangeForm
    template_name = 'accounts/detail_update_view.html'
    success_message = _("Your account %(email)s was updated successfully!")
    error_message = _('Please correct the errors below.')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = _('Change Your Account Details')
        return context

    def get_success_url(self):
        return reverse("accounts:home")


class UserPasswordChangeView(LoginRequiredMixin,
                             SuccessMessageMixin,
                             ErrorMessageMixin,
                             FormView):
    form_class = PasswordChangeForm
    template_name = 'accounts/change_password.html'
    success_message = _("Your password was successfully updated!")
    error_message = _('Please correct the errors below.')

    def get_form_kwargs(self):
        kwargs = super(UserPasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super(UserPasswordChangeView, self).form_valid(form)

    def get_success_url(self):
        return reverse("accounts:home")

    def get_context_data(self, *args, **kwargs):
        context = super(UserPasswordChangeView, self).get_context_data(*args, **kwargs)
        context['title'] = _('Password change')
        return context
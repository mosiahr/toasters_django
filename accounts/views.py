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


# from .models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

#def register(request):
#    #if request.user.is_authenticated:
#    #    logout(request)
#    context = {
#        'title': 'Регистрация',
#        'title_header': 'Пожалуйста зарегистрируйтесь',
#    }
#
#    if request.GET:
#        if request.GET['next']:
#            request.session['next'] = request.GET['next']
#
#    if request.POST:
#        form = RegisterForm(request.POST or None)
#
#        if form.is_valid():
#            form.save()
#            user = auth.authenticate(username=form.cleaned_data['email'],
#                                        password=form.cleaned_data['password2'])
#            auth.login(request, user)
#
#            # user_profile = UserProfile(user_id=user.id,
#            #                            avatar=profile_form.cleaned_data['avatar'])
#            # user_profile.save()
#
#            try:
#                return redirect('login')
#            except KeyError:
#                return redirect('toast:toasters')
#        else:
#            context['form'] = form
#            # context['profile_form'] = profile_form
#    else:
#        context['form'] = RegisterForm()
#        # context['profile_form'] = AddFieldToRegister()
#    return render(request, 'accounts/register.html', context)

#def login(request):
#    # if request.user.is_authenticated:
#    #     auth.logout(request)
#    template_response = views.login(request,
#                                    template_name='login.html',
#                                    authentication_form=LoginForm,
#                                    extra_context={
#                                        'title': _('Log in'),
#                                        # 'user': request.user,
#                                    })
#                                    # extra_context={'next': '/games/all/'})
#                                    # extra_context={'next': '/games/all/'})
#    return template_response


from toast.views import ToasterListView

class AccountHomeView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/home.html'

    def get_object(self):
        return self.request.user

class AccountActivateView(View):
    def get(self, request, uid):
        try:
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None:
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')
#class AccountEmailActivateView(FormMixin, View):
#    success_url = '/login/'
#    form_class = ReactivateEmailForm
#    key = None
#    def get(self, request, key=None, *args, **kwargs):
#        self.key = key
#        if key is not None:
#            qs = EmailActivation.objects.filter(key__iexact=key)
#            confirm_qs = qs.confirmable()
#            if confirm_qs.count() == 1:
#                obj = confirm_qs.first()
#                obj.activate()
#                messages.success(request, "Your email has been confirmed. Please login.")
#                return redirect("login")
#            else:
#                activated_qs = qs.filter(activated=True)
#                if activated_qs.exists():
#                    reset_link = reverse("password_reset")
#                    msg = """Your email has already been confirmed
#                    Do you need to <a href="{link}">reset your password</a>?
#                    """.format(link=reset_link)
#                    messages.success(request, mark_safe(msg))
#                    return redirect("login")
#        context = {'form': self.get_form(),'key': key}
#        return render(request, 'registration/activation-error.html', context)
#
#    def post(self, request, *args, **kwargs):
#        # create form to receive an email
#        form = self.get_form()
#        if form.is_valid():
#            return self.form_valid(form)
#        else:
#            return self.form_invalid(form)
#
#    def form_valid(self, form):
#        msg = """Activation link sent, please check your email."""
#        request = selfrequest
#        messages.success(request, msg)
#        email = form.cleaned_data.get("email")
#        obj = EmailActivation.objects.email_exists(email).first()
#        user = obj.user
#        new_activation = EmailActivation.objects.create(user=user, email=email)
#        new_activation.send_activation()
#        return super(AccountEmailActivateView, self).form_valid(form)
#
#    def form_invalid(self, form):
#        context = {'form': form, "key": self.key }
#        return render(self.request, 'registration/activation-error.html', context)

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



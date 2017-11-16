from django.shortcuts import render,  redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views
from django.contrib import auth
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
    UserChangeForm,
)


from django.views.generic import FormView, CreateView, DetailView


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
# from django.contrib.auth import get_user_model
#
# User = get_user_model()

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



def logout(request):
    auth.logout(request)
    return redirect('/toasters/')

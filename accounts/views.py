from django.shortcuts import render,  redirect
from django.contrib.auth import views
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm, UserChangeForm

from .forms import (
    MyAuthenticationForm,
    # MyPasswordChangeForm,
    # RegisterForm,
    # UpdateUserForm,
    # AddFieldToRegister
)
from django.utils.translation import ugettext as _

# from .models import UserProfile
# from django.contrib.auth import get_user_model
#
# User = get_user_model()

def register(request):
    if request.user.is_authenticated:
        logout(request)
    context = {
        'title': 'Регистрация',
        'title_header': 'Пожалуйста зарегистрируйтесь',
    }

    if request.GET:
        if request.GET['next']:
            request.session['next'] = request.GET['next']

    if request.POST:
        form = UserCreationForm(request.POST or None)

        if form.is_valid():
            form.save()
            user = auth.authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password2'])
            auth.login(request, user)

            # user_profile = UserProfile(user_id=user.id,
            #                            avatar=profile_form.cleaned_data['avatar'])
            # user_profile.save()

            try:
                return redirect(request.session['next'])
            except KeyError:
                return redirect('toast:toaster')
        else:
            context['form'] = form
            # context['profile_form'] = profile_form
    else:
        context['form'] = UserCreationForm()
        # context['profile_form'] = AddFieldToRegister()
    return render(request, 'register.html', context)

def login(request):
    if request.user.is_authenticated:
        auth.logout(request)
    template_response = views.login(request,
                                    template_name='login.html',
                                    # authentication_form=MyAuthenticationForm,
                                    extra_context={
                                        'title': _('Log in'),
                                    })
                                    # extra_context={'next': '/games/all/'})
    return template_response


def logout(request):
    auth.logout(request)
    return redirect('/toasters/')

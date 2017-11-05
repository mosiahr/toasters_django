from django.shortcuts import render,  redirect
from django.contrib.auth import views
from django.contrib import auth

from .forms import (
    MyAuthenticationForm,
    # MyPasswordChangeForm,
    # RegisterForm,
    # UpdateUserForm,
    # AddFieldToRegister
)
from django.utils.translation import ugettext as _

# from django.contrib.auth import get_user_model
#
# User = get_user_model()


def login(request):
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
    UserChangeForm
)
from django.forms.utils import ErrorList



class DivErrorList(ErrorList):
    def __init__(self, initlist=None, error_class=None):
        super(ErrorList, self).__init__(initlist)

        if error_class is None:
            self.error_class = 'alert alert-danger'
        else:
            self.error_class = 'alert alert-danger {}'.format(error_class)



class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList

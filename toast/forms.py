#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from django.forms import ModelForm, ModelChoiceField, MultiValueField
from django import forms

from .models import Location


from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
User = get_user_model()


class ToasterLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location_select']

    location_select = forms.ModelChoiceField(
        queryset=None,
        to_field_name='slug',
        empty_label=_('choose'),    #выбрать
        required=False,
        label=_('City'),
        # initial={'name': 'Киев'}
    )

    def __init__(self, *args, **kwargs):
        super(ToasterLocationForm, self).__init__(*args, **kwargs)
        # self.fields['location_select'].queryset = Toaster.pub_objects.filter(locations__slug=location)
        self.fields['location_select'].queryset = Location.objects.all()


# class ProfileCreateForm(forms.ModelForm):
#     # user = forms.ChoiceField(widget=forms.HiddenInput())
#
#     name = forms.CharField(
#         label=_('Name'),
#         required=False,
#         widget=forms.TextInput(attrs={
#             # "class": 'form-control',
#             "autofocus": True,
#             'placeholder': ''
#         })
#     )
#
#     email = forms.EmailField(
#         label=_('Email'),
#         # widget=forms.TextInput(attrs={'readonly': True}),
#         required=False,
#     )
#
#     class Meta:
#         model = Profile
#         # fields = ['full_name', 'email']
#         fields = ('name', 'address', 'email', 'phone', 'site', 'description', 'img', 'locations', 'tags')
#
#     #
#     # def save(self, commit=True):
#     #     # Save the provided password in hashed format
#     #     user = super(ProfileCreateForm, self).save(commit=False)
#     #     user.user_id = User.objects.get(pk=)
#     #     if commit:
#     #         user.save()
#     #     return user
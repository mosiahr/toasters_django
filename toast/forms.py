#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.forms import ModelForm, ModelChoiceField, MultiValueField
from .models import ToasterLocation, Toaster


class ToasterLocationForm(ModelForm):
    class Meta:
        model = ToasterLocation
        fields = ['location_select']

    location_select = ModelChoiceField(queryset=None,  to_field_name='slug')

    def __init__(self, *args, **kwargs):
        super(ToasterLocationForm, self).__init__(*args, **kwargs)
        # self.fields['location_select'].queryset = Toaster.pub_objects.filter(locations__slug=location)
        self.fields['location_select'].queryset = ToasterLocation.objects.all()
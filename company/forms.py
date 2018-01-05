# from django.forms import ModelForm, ModelChoiceField, MultiValueField
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model

from .models import Location, TypeCompany, Price

User = get_user_model()


# class CompanyLocationForm(forms.ModelForm):
#     class Meta:
#         model = Location
#         fields = ['location_select']
#
#     location_select = forms.ModelChoiceField(
#         queryset=None,
#         to_field_name='slug',
#         empty_label=_('choose'),    #выбрать
#         required=False,
#         label=_('City'),
#         # initial={'name': 'Киев'}
#     )
#
#     def __init__(self, *args, **kwargs):
#         super(CompanyLocationForm, self).__init__(*args, **kwargs)
#         # self.fields['location_select'].queryset = Company.pub_objects.filter(locations__slug=location)
#         self.fields['location_select'].queryset = Location.objects.all()


class CompanyLocationForm(forms.Form):
    LOCATION = [('', 'Любой')] + [(l.slug, l.name) for l in Location.objects.all()]
    TYPE = [('', 'Любой')] + [(t.slug, t.name) for t in TypeCompany.objects.all()]
    PRICE = [('', 'Любая')] + [(p.slug, p.name) for p in Price.objects.all()]

    def __init__(self, *args, **kwargs):
        super(CompanyLocationForm, self).__init__(*args, **kwargs)

        self.fields['type_company'] = forms.ChoiceField(
            choices=self.TYPE,
            required=False,
            label=_('Type'),
            widget=forms.Select()
        )

        self.fields['location_select'] = forms.ChoiceField(
            label=_('City'),
            choices=self.LOCATION,
            required=False,
            # initial={'location_select': 'Киев'},
            initial=self.LOCATION[0][0],
        )

        self.fields['price'] = forms.ChoiceField(
            choices=self.PRICE,
            required=False,
            label=_('Price'),
            widget=forms.Select()
        )

        # self.fields['type_company'].initial = 'vedushie-tamada'
    field_order = ('type_company', 'location_select', 'price')


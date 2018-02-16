# from django.forms import ModelForm, ModelChoiceField, MultiValueField
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model

from .models import (
    Location,
    TypeCompany,
    Price,
    Company
)

User = get_user_model()


class CompanyLocationForm(forms.Form):
    try:
        LOCATION = [('', 'Любой')] + [(l.slug, l.name) for l in Location.pub_objects.all()]
    except:
        LOCATION = None

    try:
        TYPE = [('', 'Любой')] + [(t.slug, t.name) for t in TypeCompany.pub_objects.all()]
    except:
        TYPE = None

    try:
        PRICE = [('', 'Любая')] + [(p.slug, p.name) for p in Price.pub_objects.all()]
    except:
        PRICE = None

    def __init__(self, *args, **kwargs):
        super(CompanyLocationForm, self).__init__(*args, **kwargs)

        self.fields['type_company'] = forms.ChoiceField(
            choices=self.TYPE,
            required=False,
            # label=_('<i class="fa fa-map-marker-alt fa-lg" aria-hidden="true"></i>&nbsp;Type'),
            label=self.set_label('fas fa-microphone fa-lg', _("Type")),
            widget=forms.Select(),
        )

        self.fields['location_select'] = forms.ChoiceField(
            label=self.set_label('fa fa-map-marker-alt fa-lg', _('City'), color='#ff253a'),
            choices=self.LOCATION,
            required=False,
            # initial=self.LOCATION[0][0],
        )
        # self.fields['location_select'].widget.attrs.update({'class': 'fa-map-marker-alt'})

        self.fields['price'] = forms.ChoiceField(
            choices=self.PRICE,
            required=False,
            label=self.set_label('fas fa-dollar-sign fa-lg', _('Price'), color='green'),
            widget=forms.Select()
        )
        # self.fields['type_company'].initial = 'vedushie-tamada'

    def set_label(self, fontawesome, label, color=None):
        return '<i class="{0} " style="color: {2}"></i> {1}'.format(fontawesome, label, color)

    field_order = ('type_company', 'location_select', 'price')


class CompanyAddForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'type', 'address', 'email', 'phone',
                  'site', 'description', 'img', 'locations', 'tags', 'price')
        text = 'Hold down "Control", or "Command" on a Mac, to select more than one.'
        help_texts = {
            'type': _(text),
            'locations': _(text),
            'tags': _(text),
        }


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'type', 'address', 'email', 'phone',
                  'site', 'description', 'img', 'locations', 'tags', 'price')
        text = 'Hold down "Control", or "Command" on a Mac, to select more than one.'
        help_texts = {
            'type': _(text),
            'locations': _(text),
            'tags': _(text),
        }


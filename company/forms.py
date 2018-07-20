from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model

# from easy_select2 import select2_modelform, select2_modelform_meta
from easy_select2.widgets import Select2, Select2Multiple
# from easy_select2.utils import apply_select2


from .models import (
    Location,
    TypeCompany,
    Price,
    Company
)
from tags.models import Tag
from gallery.models import Album


User = get_user_model()


class CompanyFilterForm(forms.Form):
    try:
        TYPE = [('', '')] + [(t.slug, t.name) for t in TypeCompany.pub_objects.all()]
    except:
        TYPE = None

    try:
        LOCATION = [('', '')] + [(l.slug, l.name) for l in Location.pub_objects.all()]
    except:
        LOCATION = None

    try:
        PRICE = [('', '')] + [(p.slug, p.name) for p in Price.pub_objects.all()]
    except:
        PRICE = None

    def __init__(self, *args, **kwargs):
        super(CompanyFilterForm, self).__init__(*args, **kwargs)

        self.fields['type'] = forms.ChoiceField(
            choices=self.TYPE,
            required=False,
            # label=_('<i class="fa fa-map-marker-alt fa-lg" aria-hidden="true"></i>&nbsp;Type'),
            label=self.set_label('fas fa-microphone fa-lg', _('Type'), color='white'),
            widget=forms.Select(attrs={
                'class': 'form-select2-type',
            })
        )

        self.fields['location'] = forms.ChoiceField(
            label=self.set_label('fa fa-map-marker-alt fa-lg', _('City'), color='white'),
            choices=self.LOCATION,
            required=False,
            # initial=self.LOCATION[0][0],
            widget=forms.Select(attrs={
                'class': 'form-select2-city',
            }),
        )
        # self.fields['location_select'].widget.attrs.update({'class': 'fa-map-marker-alt'})

        self.fields['price'] = forms.ChoiceField(
            choices=self.PRICE,
            required=False,
            label=self.set_label('fas fa-dollar-sign fa-lg', _('Price'), color='white'),
            widget=forms.Select(attrs={
                'class': 'form-select2-price',
            }),
        )
        # self.fields['type_company'].initial = 'vedushie-tamada'

    def set_label(self, fontawesome, label, color=None):
        return '<i class="{0} " style="color: {2}"></i> {1}'.format(fontawesome, label, color)

    field_order = ('type', 'location', 'price')


class CompanyAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompanyAddForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget.attrs = {'class': 'form-select2-type'}
        self.fields['location'].widget.attrs = {'class': 'form-select2-city'}
        self.fields['price'].widget.attrs = {'class': 'form-select2-price'}

    class Meta:
        model = Company
        fields = ('name', 'type', 'address', 'email', 'phone',
                  'site', 'description', 'avatar',
                  # 'album',
                  'location', 'tags', 'price')
        text = 'Hold down "Control", or "Command" on a Mac, to select more than one.'
        help_texts = {
            # 'type': _(text),
            'location': _(text),
            'tags': _(text),
        }


class CompanyUpdateForm(CompanyAddForm):
    # def __init__(self, *args, **kwargs):
    #     super(CompanyUpdateForm, self).__init__(*args, **kwargs)
    #     self.fields['album'] = forms.ModelMultipleChoiceField(queryset=Album.objects.filter(company__id=kwargs['instance'].id))
    pass
# from django.forms import ModelForm, ModelChoiceField, MultiValueField
from django import forms

from .models import Location, TypeCompany


from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
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
    LOCATION = [('', '---------')] + [(l.slug, l.name) for l in Location.objects.all()]
    TYPE = [('', '---------')] + [(t.slug, t.name) for t in TypeCompany.objects.all()]

    def __init__(self, *args, **kwargs):
        super(CompanyLocationForm, self).__init__(*args, **kwargs)
        # print(self.LOCATION)
        self.fields['location_select'] = forms.ChoiceField(
            label=_('City'),
            choices=self.LOCATION,
            required=False,
            # initial={'location_select': 'Киев'},
            initial=self.LOCATION[0][0]
        )

        self.fields['type_company'] = forms.ChoiceField(
            choices=self.TYPE,
            required=False,
            label=_('Type'),
            widget=forms.Select()
        )


        # self.fields['location_select'].queryset = Company.pub_objects.filter(locations__slug=location)
        # self.fields['location_select'].queryset = Location.objects.all()
        # self.fields['type_company'].queryset = TypeCompany.objects.all()



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
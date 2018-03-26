from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Fieldset, SplitDateTimeField, Row, Column, ButtonHolder, Submit
from crispy_forms_foundation.layout.buttons import Button
from django.forms import inlineformset_factory

from django.utils.translation import ugettext as _
from .models import Photo, Album
from company.models import Company


class PhotoAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhotoAddForm, self).__init__(*args, **kwargs)
        # self.fields['type'].widget.attrs = {"class": 'form-select2'}
        # self.fields['location'].widget.attrs = {"class": 'form-select2'}
        # self.fields['tags'].widget.attrs = {"class": 'form-select2'}

    class Meta:
        model = Photo
        fields = ('name', 'title', 'image', 'album', 'is_cover_photo')
        # text = 'Hold down "Control", or "Command" on a Mac, to select more than one.'
        # help_texts = {
        #     'type': _(text),
        #     'location': _(text),
        #     'tags': _(text),
        # }


class AlbumForm(forms.ModelForm):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'required':''}),
        required=True
    )
    slug = forms.CharField(label=_('Slug'), required=True)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()

        # Enable Abide validation on the form
        self.helper.attrs = {'data_abide': '', 'novalidate': ''}

        self.helper.form_action = '.'

        self.helper.form_tag = False

        # self.helper.layout = Layout(
            # Fieldset(
            #     _('Album'),
            #     'name',
            #     'slug',
            #     'summary'
            # ),
            # Fieldset(
            #     'Display settings',
            #     Row(
            #         Column('name', css_class='large-6'),
            #         Column('slug', css_class='large-3'),
            #         Column('summary', css_class='large-3'),
            #     ),
            # ),
            # Fieldset(
            #     'Publish settings',
            #     'parent',
            #     Row(
            #         Column(SplitDateTimeField('published'), css_class='large-6'),
            #         Column('slug', css_class='large-6'),
            #     ),
            # ),
            # ButtonHolder(
            #     # HTML('<span style = "display: hidden;" > Information Saved </span>'),
            #     Submit('submit', _('Save'), css_class='success'),
            #     Button('cancel', _('Cancel'), css_class='secondary'),
            # ),
        # )
        super(AlbumForm, self).__init__(*args, **kwargs)
        # self.fields['name'].abide_msg = "This field is required !"



    class Meta:
        model = Album
        # fields = ('name', 'slug', 'summary')
        exclude = ()


class PhotoForm(forms.ModelForm):
    # image =
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.attrs = {'data_abide': '', 'novalidate': ''}
        # self.helper.form_tag = False

        super(PhotoForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Photo
        fields = ('name', 'title', 'image', 'is_cover_photo')


# class PhotoFormHelper(FormHelper):
#     def __init__(self, *args, **kwargs):
#         super(PhotoFormHelper, self).__init__(*args, **kwargs)
#         self.form_tag = False
#         self.layout = Layout(
#             Fieldset("Add photo",
#                      'name',
#                      'title',
#                      'image',
#                      ),
#         )


PhotoFormSet = inlineformset_factory(
    Album,
    Photo,
    form=PhotoForm,
    fields=[
        'name',
        'title',
        'is_cover_photo',
        'image'
    ],
    extra=1)

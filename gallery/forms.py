from django import forms
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
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(AlbumForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Album
        fields = ('name', 'summary')

    def save(self, commit=True):
        instance = super(AlbumForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance


class PhotoForm(forms.ModelForm):
    image = forms.ImageField(
        label=_('Image'),
        required=True,
    )

    class Meta:
        model = Photo
        fields = ('name', 'title', 'image', 'is_cover_photo')


PhotoFormSet = inlineformset_factory(
    Album,
    Photo,
    form=PhotoForm,
    # max_num=30,
    # can_delete=True,
    )

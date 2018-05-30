from django import forms
from django.forms import inlineformset_factory


from django.utils.translation import ugettext as _
from .models import Photo, Album
from company.models import Company


class PhotoAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhotoAddForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'initial':_('Portfolio')}
        # self.fields['type'].widget.attrs = {"class": 'form-select2'}
        # self.fields['location'].widget.attrs = {"class": 'form-select2'}
        # self.fields['tags'].widget.attrs = {"class": 'form-select2'}

    class Meta:
        model = Photo
        fields = ('name', 'title', 'image', 'album', 'is_cover_photo')


class AlbumForm(forms.ModelForm):
    name = forms.CharField(initial=_('Portfolio'))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AlbumForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Album
        fields = ('name', 'summary')

    def save(self, commit=True):
        instance = super(AlbumForm, self).save(commit=False)
        instance.user = self.user
        instance.company = Company.pub_objects.filter(user_id=self.user).first()
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
    # min_num=1,
    )



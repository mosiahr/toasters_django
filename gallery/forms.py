from django import forms
from django.utils.safestring import mark_safe
from django.forms import inlineformset_factory
from django.utils.translation import ugettext as _
from .models import Photo, Album
from company.models import Company


class PhotoAddForm(forms.ModelForm):
    label_img = _('Choose a file')

    image = forms.ImageField(
        label=mark_safe(
            "<a class='button button-addfile expanded'"
            " for='id_image'><i class='fas fa-upload fa-lg'></i>&nbsp;<span>{}</span></a>"
                .format(label_img)),
        # label="Add",
        label_suffix='',
        required=True,
        widget=forms.FileInput(
            attrs={
                'class': 'inputfile',
            }
        )
    )

    name = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                # 'autofocus': True,
                'placeholder': _('Name'),
            }
        ),
    )
    title = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Title'),
            }
        ),
    )

    is_cover_photo = forms.BooleanField(
        label=_('Cover photo'),
        label_suffix='',
        required=False,
        widget=forms.CheckboxInput()
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PhotoAddForm, self).__init__(*args, **kwargs)
        albums = Album.pub_objects.filter(user_id=self.user.id)
        self.fields['album'] = forms.ModelChoiceField(
            queryset=albums,
            label='',
            required=True,
            widget=forms.Select(
                attrs={
                    'class': 'form-select2-addPhoto',
                }
            ),
        )

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



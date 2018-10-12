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
                'placeholder': _('Name (optional field)'),
            }
        ),
    )

    is_cover_photo = forms.BooleanField(
        # label=_('Cover photo'),
        label=mark_safe(
            "{}<input type='checkbox' name='is_cover_photo'"
            " id='id_is_cover_photo'><span class='checkmark'></span>".format(_('Is cover photo'))
        ),
        label_suffix='',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                # 'class': 'checkmark'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PhotoAddForm, self).__init__(*args, **kwargs)
        albums = Album.pub_objects.filter(author=self.user)
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
        fields = ('name', 'image', 'album', 'is_cover_photo')

    def save(self, commit=True):
        instance = super(PhotoAddForm, self).save(commit=False)
        instance.author = self.user
        if commit:
            instance.save()
        return instance


class AlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(AlbumForm, self).__init__(*args, **kwargs)
        count_album = Album.pub_objects.filter(author=self.user).count()
        self.fields['name'] = forms.CharField(initial='{} {}'.format(_('Portfolio'), count_album + 1))

    class Meta:
        model = Album
        fields = ('name', 'summary')

    def save(self, commit=True):
        instance = super(AlbumForm, self).save(commit=False)
        instance.author = self.user
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
        fields = ('name', 'image', 'is_cover_photo')

PhotoFormSet = inlineformset_factory(
    Album,
    Photo,
    form=PhotoForm,
    # form=PhotoAddForm,
    # max_num=30,
    # can_delete=True,
    # min_num=1,
)

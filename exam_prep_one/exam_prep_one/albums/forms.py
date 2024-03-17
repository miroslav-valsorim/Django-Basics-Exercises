from django import forms

from exam_prep_one.albums.models import Album


class ReadonlyFieldsFormMixin:
    readonly_fields = ()

    def _apply_readonly_on_fields(self):
        for field_name in self.readonly_field_names:
            self.fields[field_name].widget.attrs['readonly'] = 'readonly'

    @property
    def readonly_field_names(self):
        if self.readonly_fields == '__all__':
            return self.fields.keys()

        return self.readonly_fields


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']

        labels = {
            'image_url': 'Image URL'
        }

        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'})
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadonlyFieldsFormMixin,AlbumBaseForm):
    readonly_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


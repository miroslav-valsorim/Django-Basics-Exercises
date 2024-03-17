from django import forms

from exam_prep_two.fruits.models import Fruits


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


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruits
        exclude = ['owner', ]

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }


class EditFruitForm(CreateFruitForm):
    class Meta:
        model = Fruits
        exclude = ['owner', ]


class DeleteFruitForm(ReadonlyFieldsFormMixin, CreateFruitForm):

    readonly_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

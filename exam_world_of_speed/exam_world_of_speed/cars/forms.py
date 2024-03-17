from django import forms

from exam_world_of_speed.cars.models import Car


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


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner', ]


class CreateCarForm(CarForm):
    class Meta:
        model = Car
        exclude = ['owner', ]

        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://'})
        }


class EditCarForm(CarForm):
    pass


class DeleteCarForm(ReadonlyFieldsFormMixin, CarForm):
    readonly_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

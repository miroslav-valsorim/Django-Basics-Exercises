from django import forms
from django.forms import modelform_factory

from forms_advanced.web.models import Person


class ReadOnlyFieldsForm:
    readonly_fields = ()

    def _mark_readonly_fields(self):
        for field_name in self.readonly_fields:
            self.fields[field_name].widget.attrs['readonly'] = 'readonly'
        # for _, field in self.fields.items():
        #     field.widget.attrs['readonly'] = 'readonly'


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        # print(cleaned_data)
        return cleaned_data

    # def clean_first_name(self):
    #     pass

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user.is_authenticated:
            instance.created_by = self.user
        instance.save()
        return instance


class UpdatePersonForm(ReadOnlyFieldsForm, PersonForm):
    readonly_fields = ('age', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self._mark_readonly_fields()


PersonForm2 = modelform_factory(Person, fields='__all__')

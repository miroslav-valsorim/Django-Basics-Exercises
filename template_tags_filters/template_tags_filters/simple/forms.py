from django import forms

from template_tags_filters.simple.models import Person


class SimpleForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)

    age = forms.IntegerField(required=True)

    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')], required=True,
    )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


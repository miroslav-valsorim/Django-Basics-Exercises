from django import forms

from forms_first_excercise.model_form.models import Person


class PersonFormModel(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'last_name', 'age', 'email']  # or __all__
        # exclude = ['name']  exclude rows

        labels = {
            'name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'email': 'Email',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your last name'
                }
            )
        }

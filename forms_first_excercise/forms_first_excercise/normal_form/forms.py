from django import forms


class PersonForm(forms.Form):

    first_name = forms.CharField(
        max_length=35,
        required=True,
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your first name'
            }
        )
    )

    last_name = forms.CharField(
        max_length=35,
        required=True,
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your last name'
            }
        )
    )

    age = forms.IntegerField(
        required=True,
    )

    email = forms.EmailField()

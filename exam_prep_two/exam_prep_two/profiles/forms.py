from django import forms

from exam_prep_two.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['owner', 'age', 'image_url']

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class EditProfileForm(CreateProfileForm):
    class Meta:
        model = Profile
        exclude = ['owner', 'password', 'email']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age',
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['password', 'image_url', 'first_name', 'last_name', 'email', 'age']

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

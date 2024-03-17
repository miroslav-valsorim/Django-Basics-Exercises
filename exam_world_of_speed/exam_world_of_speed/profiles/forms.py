from django import forms

from exam_world_of_speed.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['owner', 'first_name', 'last_name', 'profile_picture', ]

        widgets = {
            'password': forms.PasswordInput()
        }


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    class Meta:
        model = Profile
        exclude = ['owner', ]


class DeleteProfileForm(ProfileForm):
    class Meta:
        model = Profile
        exclude = ['owner', 'first_name', 'last_name', 'profile_picture', 'password', 'email', 'username', 'age']

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


from django import forms

from exam_prep_one.profiles.models import Profile


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = '__all__'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


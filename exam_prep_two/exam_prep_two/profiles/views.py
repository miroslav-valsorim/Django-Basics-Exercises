from django.shortcuts import render, redirect

from exam_prep_two.mainpage.views import get_profile
from exam_prep_two.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from exam_prep_two.profiles.models import Profile


# Create your views here.

def create_profile(request):
    create_form = CreateProfileForm(request.POST or None)

    profile = get_profile()
    no_profile = False

    if profile is None:
        no_profile = True

    if request.method == 'POST':
        if create_form.is_valid():
            create_form.save()
            return redirect('dashboard')

    context = {
        'create_form': create_form,
        'no_profile': no_profile,
    }

    return render(request, 'profiles/create-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    edit_profile_form = EditProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return redirect('details_profile',)

    context = {
        'profile': profile,
        'edit_profile_form': edit_profile_form,
    }

    return render(request, 'profiles/edit-profile.html', context)


def details_profile(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }

    return render(request, 'profiles/details-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    delete_form = DeleteProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        delete_form.save()
        return redirect('main_page')

    context = {
        'profile': profile,
        'delete_form': delete_form,
    }

    return render(request, 'profiles/delete-profile.html', context)
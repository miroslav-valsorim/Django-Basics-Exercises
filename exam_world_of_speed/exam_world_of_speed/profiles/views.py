from django.db.models import Avg, Sum
from django.shortcuts import render, redirect

from exam_world_of_speed.cars.models import Car
from exam_world_of_speed.profiles.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from exam_world_of_speed.profiles.models import Profile

'''
Profile views
'''


def create_profile(request):
    create_form = CreateProfileForm(request.POST or None)

    if request.method == 'POST':
        if create_form.is_valid():
            create_form.save()
            return redirect('car_catalogue')

    context = {
        'create_form': create_form,
    }

    return render(request, 'profiles/profile-create.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    edit_form = EditProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if edit_form.is_valid():
            edit_form.save()
            return redirect('details_profile',)

    context = {
        'edit_form': edit_form,
    }

    return render(request, 'profiles/profile-edit.html', context)


def details_profile(request):
    profile = Profile.objects.first()

    price = Car.objects.filter(owner=profile).aggregate(sum=Sum('price'))['sum']

    context = {
        'profile': profile,
        'total_price': price or 0
    }

    return render(request, 'profiles/profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    delete_form = DeleteProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        delete_form.save()
        return redirect('index')

    context = {
        'delete_form': delete_form,
    }

    return render(request, 'profiles/profile-delete.html', context)
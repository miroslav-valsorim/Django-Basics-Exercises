from django.shortcuts import render, redirect

from exam_prep_one.profiles.forms import DeleteProfileForm
from exam_prep_one.profiles.models import Profile


# Create your views here.
def profile_details(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile-details.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    delete_form = DeleteProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        delete_form.save()
        return redirect('index')

    context = {
        'profile': profile,
        'delete_form': delete_form,
    }

    return render(request, 'profiles/profile-delete.html', context)

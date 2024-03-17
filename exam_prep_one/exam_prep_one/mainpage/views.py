from django.shortcuts import render, redirect

from exam_prep_one.albums.models import Album
from exam_prep_one.mainpage.forms import EnterProfileForm
from exam_prep_one.profiles.models import Profile


# Create your views here.
def get_profile():
    return Profile.objects.first()


def create_profile(request):
    form = EnterProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'enter_form': form,
        'no_nav': True,
    }

    return render(request, 'home/home-no-profile.html', context)


def index(request):
    profile = get_profile()
    albums = Album.objects.all()

    if profile is None:
        return create_profile(request)

    context = {
        'albums': albums,
    }

    return render(request, 'home/home-with-profile.html', context)



    # albums = Album.objects.all()
    # enter_form = EnterProfileForm(request.POST or None)
    #
    # if request.method == 'POST':
    #     if enter_form.is_valid():
    #         enter_form.save()
    #
    # context = {
    #     'albums': albums,
    #     'enter_form': enter_form,
    # }
    # profile = get_profile()
    #
    # if profile is not None:
    #     return render(request, 'home/home-with-profile.html', context)
    #
    # return render(request, 'home/home-no-profile.html', context)

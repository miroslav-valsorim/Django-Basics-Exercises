from django.shortcuts import render

from exam_prep_two.fruits.models import Fruits
from exam_prep_two.profiles.models import Profile

'''
MAINPAGE VIEWS
'''


def get_profile():
    return Profile.objects.first()


def main_page(request):
    profile = get_profile()
    no_profile = False

    if profile is None:
        no_profile = True

    context = {
        'no_profile': no_profile,
    }

    return render(request, 'mainpage/index.html', context)


def dashboard(request):
    profile = get_profile()
    fruits = Fruits.objects.all()

    context = {
        'fruits': fruits,
        'profile': profile,
    }
    return render(request, 'mainpage/dashboard.html', context)

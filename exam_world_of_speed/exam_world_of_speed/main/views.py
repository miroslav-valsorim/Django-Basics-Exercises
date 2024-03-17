from django.shortcuts import render

from exam_world_of_speed.profiles.models import Profile

'''
main page views
'''


def index(request):
    profile = Profile.objects.first()

    no_profile = False

    if profile is None:
        no_profile = True

    context = {
        'no_profile': no_profile,
    }

    return render(request, 'main/index.html', context)

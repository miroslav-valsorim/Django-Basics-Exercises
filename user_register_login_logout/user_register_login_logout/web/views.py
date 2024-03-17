from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins


# Create your views here.

def index(request):
    return render(request, 'home/index.html')


# shows the view only to logged person with FBV
@login_required
def about(request):
    context = {
        'user': request.user
    }
    return render(request, 'home/about.html', context)


# shows the view only to logged person with CBV
class TeamView(auth_mixins.LoginRequiredMixin, views.View):
    def get(self, request):
        return HttpResponse(f"{request.user}'s team!")

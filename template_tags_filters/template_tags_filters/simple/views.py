from django.shortcuts import render, redirect

from template_tags_filters.simple.forms import SimpleForm, PersonForm
from template_tags_filters.simple.models import Person


def index(request):

    if request.method == 'POST':
        modelform = PersonForm(request.POST)
    else:
        modelform = PersonForm()

    if request.method == 'POST':
        if modelform.is_valid():
            modelform.save()
            return redirect('index')

    context = {
        'form': SimpleForm(),
        'modelform': modelform,
        'users': Person.objects.all(),
        'random_numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    }
    return render(request, 'main_page/index.html', context)

#
# def update_user(request, pk):
#     user = Person.objects.get(pk=pk)
#
#     if request.method == 'POST':
#         modelform = PersonForm(request.POST, instance=user)
#     else:
#         modelform = PersonForm(instance=user)
#
#     if request.method == 'POST':
#         if modelform.is_valid():
#             modelform.save()
#             return redirect('index')
#
#     context = {
#         'modelform_update': modelform,
#         'personal_pk': user,
#     }
#     return render(request, 'main_page/index.html', context)
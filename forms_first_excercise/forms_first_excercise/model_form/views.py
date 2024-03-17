from django.forms import ModelForm
from django.shortcuts import render, redirect

from forms_first_excercise.model_form.forms import PersonFormModel
from forms_first_excercise.model_form.models import Person


# Create your views here.
def model_form(request):
    if request.method == 'POST':
        form = PersonFormModel(request.POST)
    else:
        form = PersonFormModel()

    if request.method == 'POST':
        if form.is_valid():
            # print(form.cleaned_data['name'])
            # print(request.POST['name'])
            form.save()
            return redirect('model_form')

    context = {
        'model_form_context': form,
        'peoples_list': Person.objects.all(),
    }

    return render(request, 'modelform/model_form.html', context)


def update_person(request, pk):
    person = Person.objects.get(pk=pk)

    if request.method == 'POST':
        form = PersonFormModel(request.POST, instance=person)
    else:
        form = PersonFormModel(instance=person)

    if request.method == 'POST':
        if form.is_valid():
            # print(form.cleaned_data['name'])
            # print(request.POST['name'])
            form.save()
            return redirect('model_form')

    context = {
        'model_form_update_context': form,
        'personal_pk': person,
    }

    return render(request, 'modelform/person_update.html', context)

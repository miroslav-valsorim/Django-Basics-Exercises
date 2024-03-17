from django.shortcuts import render

from forms_advanced.forms import PersonForm, UpdatePersonForm


def index(request):
    person_form = PersonForm()
    update_form = UpdatePersonForm()

    context = {
        "person_form": person_form,
        'update_form': update_form
    }

    return render(request, 'web/index.html', context)


def create_person(request):
    form = PersonForm(request.POST, user=request.user)

    if form.is_valid():
        form.save()

    return render(request,'web/create_person.html', {'form': form})

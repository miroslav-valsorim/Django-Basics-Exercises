from django.shortcuts import render, redirect

from exam_world_of_speed.cars.forms import CreateCarForm, EditCarForm, DeleteCarForm
from exam_world_of_speed.cars.models import Car
from exam_world_of_speed.profiles.models import Profile

'''
car views
'''


def car_create(request):
    create_car_form = CreateCarForm(request.POST or None)

    if request.method == 'POST':
        if create_car_form.is_valid():
            instance = create_car_form.save(commit=False)
            instance.owner = Profile.objects.first()
            instance.save()
            return redirect('car_catalogue')

    context = {
        'create_car_form': create_car_form
    }

    return render(request, 'cars/car-create.html', context)


def car_edit(request, id):
    car = Car.objects.get(id=id)
    edit_car_form = EditCarForm(request.POST or None, instance=car)

    if request.method == 'POST':
        if edit_car_form.is_valid():
            edit_car_form.save()
            return redirect('car_catalogue')
            # return redirect('car_details', id=id)

    context = {
        'edit_car_form': edit_car_form,
        'car': car,
    }

    return render(request, 'cars/car-edit.html', context)


def car_details(request, id):
    car = Car.objects.get(id=id)
    context = {
        'car': car,
    }

    return render(request, 'cars/car-details.html', context)


def car_delete(request, id):
    car = Car.objects.get(id=id)
    delete_car_form = DeleteCarForm(request.POST or None, instance=car)

    if request.method == 'POST':
        if delete_car_form.is_valid():
            delete_car_form.save()
            return redirect('car_catalogue')

    context = {
        'delete_car_form': delete_car_form,
        'car': car,
    }

    return render(request, 'cars/car-delete.html', context)


def car_catalogue(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()

    context = {
        'cars': cars,
        'profile': profile,
    }

    return render(request, 'cars/catalogue.html', context)
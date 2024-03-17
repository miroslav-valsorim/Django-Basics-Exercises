from django.shortcuts import render, redirect

from exam_prep_two.fruits.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from exam_prep_two.fruits.models import Fruits
from exam_prep_two.mainpage.views import get_profile


def create_fruit(request):
    create_fruit_form = CreateFruitForm(request.POST or None)

    if request.method == 'POST':
        if create_fruit_form.is_valid():
            instance = create_fruit_form.save(commit=False)
            instance.owner = get_profile()
            instance.save()
            return redirect('dashboard')

    context = {
        'create_fruit_form': create_fruit_form,
    }
    return render(request, 'fruits/create-fruit.html', context)


def edit_fruit(request, fruitId):
    fruit = Fruits.objects.filter(id=fruitId).get()
    edit_fruit_form = EditFruitForm(request.POST or None, instance=fruit)

    if request.method == 'POST':
        if edit_fruit_form.is_valid():
            edit_fruit_form.save()
            return redirect('details_fruit', fruitId=fruitId)

    context = {
        'edit_fruit_form': edit_fruit_form,
        'fruit': fruit,
    }
    return render(request, 'fruits/edit-fruit.html', context)


def details_fruit(request, fruitId):
    fruits = Fruits.objects.get(id=fruitId)
    context = {
        'fruits': fruits,
    }
    return render(request, 'fruits/details-fruit.html', context)


def delete_fruit(request, fruitId):
    fruit = Fruits.objects.get(id=fruitId)
    delete_fruit_form = DeleteFruitForm(request.POST or None, instance=fruit)

    if request.method == 'POST':
        if delete_fruit_form.is_valid():
            delete_fruit_form.save()
            return redirect('dashboard')

    context = {
        'delete_fruit_form': delete_fruit_form,
        'fruit': fruit,

    }
    return render(request, 'fruits/delete-fruit.html', context)

from django.shortcuts import render, redirect

from forms_first_excercise.normal_form.forms import PersonForm


# Create your views here.

def normal_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
    else:
        form = PersonForm()

    if request.method == 'POST':
        if form.is_valid():
            # print(form.cleaned_data['first_name'])
            # print(request.POST['first_name'])
            return redirect('normal_form')

    context = {
        'normal_form_context': form,
    }

    return render(request, 'normalform/normal_form.html', context)

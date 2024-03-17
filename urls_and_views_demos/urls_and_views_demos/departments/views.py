import time

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse(f"Response from {time.time()}")


def index2(request, *args, **kwargs):
    return HttpResponse(f"Response with {args} and {kwargs}")


def department_1_details(request):
    return HttpResponse(f"Department 1")


def department_2_details(request):
    return HttpResponse(f"Department 2")


def department_details(request, pk):
    return HttpResponse(f"Department by id: {pk}")


def department_details_by_name(request, name):
    return HttpResponse(f"Department by name: {name}")
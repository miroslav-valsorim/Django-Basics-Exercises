import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.


# def index(request, *args, **kwargs):
#     content = f"it works with args={args}, kwargs={kwargs}, <br/>" + \
#               f"path = {request.path},<br/>" + \
#               f"method = {request.method},<br/>" + \
#               f"user = {request.user}"
#
#     return HttpResponse(content)

def index(request, *args, **kwargs):
    context = {}
    return render(request, 'core/index.html')


def index_json(request, *args, **kwargs):
    content = json.dumps({
        "args": args,
        "kwargs": kwargs,
        "path": request.path,
        "method": request.method,
        "user": str(request.user),
    })

    return JsonResponse(
        content,
        # content_type="application/json",
        safe=False
    )

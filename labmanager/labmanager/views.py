from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def index(request):
    # return HttpResponse("Welcome to the lab management website")
    labname='Avi''s lab'
    return render(request,
                  'indexpage.html',
                  {'labName':labname,
                   })

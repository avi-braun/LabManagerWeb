from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail,send_mass_mail


def index(request):
    return render(request,'index.html')

def success(request):
    email=request.POST.get('email','')
    data="""


Hi,
Thank you for registering as a user at the XX lab.
All the best,
Avi
"""
    send_mail('Welcome',data,"Yasoob",
              [email],fail_silently=False)

    return render(request,'success.html')

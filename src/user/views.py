from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import logout


# Create your views here.
def index_view(request):
    return HttpResponse(str(request.user))


def signout_view(request):
    logout(request)
    return redirect('admin:login')
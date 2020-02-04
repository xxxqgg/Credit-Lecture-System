from django.shortcuts import render, HttpResponse


# Create your views here.
def index_view(request):
    return HttpResponse(str(request.user))
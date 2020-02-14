from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def index_view(request):
    return HttpResponse(str(request.user))


def signout_view(request):
    logout(request)
    return redirect('user:login')


def login_view(request):
    if request.method == 'POST':
        try:
            student_id = request.POST['id']
            password = request.POST['passcode']
            user = authenticate(request,username=student_id,password=password)
            if user is not None and user.is_active:
                login(request,user)
                return redirect('lecture:index')
        except KeyError:
            return redirect('user:login')
    else:
        return render(request,'login_page.html')
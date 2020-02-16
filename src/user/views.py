from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import logout, authenticate, login
from lecture.models import DrawResult


# Create your views here.
def index_view(request):
    if request.user.is_anonymous:
        redirect('user:login')
    draw_results = DrawResult.objects.all().filter(student=request.user)
    # TODO: Now, this only works when the user is student, come up with
    #  some other function when the user is staff

    # print(lecture_list)
    context = {
        'results': draw_results
    }
    return render(request,'lecture_chosen.html', context)


def sign_out_view(request):
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

    return render(request,'login_page.html')
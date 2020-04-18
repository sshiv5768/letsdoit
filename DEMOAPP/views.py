from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib import messages
from .models import SubmitTask
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User


# Create your views here.


def home(request):
    # if request.user.is_anonymous:
        # return redirect("/login/")
    return render(request, 'index.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'Login.html')

    return render(request, 'Login.html')


def logoutuser(request):
    logout(request)
    return redirect("/")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.save()
        messages.success(request, 'Successfully Created!')
        return redirect('/login/')

    else:
        return render(request, 'Sign_up.html')


def about_us(request):
    return render(request, 'about_us.html')


def submit_task(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        submit = SubmitTask(first_name=first_name, last_name=last_name,
                            address=address,
                            phone=phone, city=city,
                            state=state, zip=zip)
        submit.save()
        messages.success(request, 'Successfully Submitted!')
    return render(request, 'submit_task.html')


def submit_health(request):
    return render(request, 'submit_health.html')

from django.shortcuts import render, HttpResponse
from . import urls
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Contact,Appointment
from django.shortcuts import redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'index.html')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)

        user = authenticate(username=username, password=password)
        # print(1)
        # print(user)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return render(request, 'index.html', {'name': request.user.username})
        else:

            return render(request, 'login.html')

    return render(request, 'login.html')


def registeruser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'login.html')

    return render(request, 'register.html')


def user(request):
    return render(request, 'user.html')


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        con = Contact(name=name, subject=subject, Email=email, message=message)
        con.save()
        return render(request, 'contact.html')
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')


def departments(request):
    return render(request, 'depatments.html')


def doctor(request):
    return render(request, 'doctor.html')


def about(request):
    return render(request, 'about.html')


def appointment(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            date_time = request.POST.get('date_time')
            date,time,am_pm=date_time.split(' ')
            time=time+am_pm
            ap=Appointment(name=name,gender=gender,Email=email,date_time=date,time=time)
            ap.save()
            return render(request,'videocallUser.html')
    else:
        return redirect('loginuser')
        
    
    
        
        

    return render(request, 'appointment.html')


@login_required
def videocall(request):
    
    if request.method == 'POST':
        roomID = request.POST.get('roomID')

        shared_link = {
            
            'url': f'{request.scheme}://{request.get_host()}{request.path}?roomID={roomID}',
        }
       
        subject = 'Your appointment from DocNow'
        message = f'Click to connect to our Doctor {shared_link}, '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email]
        
       
        send_mail( subject, message, email_from, recipient_list )
        

        # Handle the roomID value in your view logic
       

        # You can also send a response back to the JavaScript code

    return render(request, 'videocall.html',{'name':request.user.username})


def videocallUser(request):
    if request.method == 'POST':
        return render(request,'success.html')
    
    return render(request, 'videocallUser.html')


def logoutuser(request):

    logout(request)
    return redirect('/')
def success(request):

    return render(request,'success.html')

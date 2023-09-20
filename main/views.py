from django.shortcuts import render, redirect
from .models import policeStation, emergency, user, complaint
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import ssl 
# import certifi from urllib.request 
# import urlopen 

# request = "https://nd-123-456-789.p2pify.com/901c7d18b72538fd3324248e1234" 
# urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))

# Create your views here.
def registerView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['cpassword']
        if (password == c_password):
            NEWUSER = user.objects.create(
            email = email,
            password = password
            )
            NEWUSER.save()
            request.session['user_id'] = NEWUSER.id
            return render(request, 'pstation.html')
        else:
            messages.error(request, "Password and confirm password does not match")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def loginView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        CHECKUSER = user.objects.get(email = email)
        if CHECKUSER:
            if email == CHECKUSER.email and password == CHECKUSER.password:
                request.session['user_id'] = CHECKUSER.id
                messages.success(request, "Now you are logged in")
                return redirect('stationsView')
            else:
                messages.error(request, "Email and password does not match")
                return render(request, 'login.html')
        else: 
            messages.error(request, "Email and password does not match")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
def logout(request):
    if 'user_id' in request.session:
        token = request.session.get('user_id')
        del request.session['user_id']
        request.session.pop('user_id', None)
        messages.success(request, "You are logged out")
        return render(request, 'login.html')
    else:
        messages.error(request, "You are not logged in")
        return render(request, 'login.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def sendOtp(request):
    if request.POST:
        email = request.POST['email']
        CHECKUSER = user.objects.get(email=email)
        if CHECKUSER:
            otp = random.randint(1111, 9999)
            CHECKUSER.otp = otp
            CHECKUSER.save()
            subject = f"OTP verify - {otp} | Epolice"
            message = f"Your OTP is : {otp}"
            send_mail(subject, message, "mauryasnehal99@gmail.com", [email,])
            messages.success(request, "Please check your email")
            return render(request, 'otpVerify.html', {'email':email})
        else:
            messages.error(request, "This email is not exist")
            return redirect('loginView')
    else:
        return render(request, 'forgotpassword.html')
    
def otpVerify(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        npassword = request.POST['npassword']
        cpassword = request.POST['cpassword']
        CHECKUSER = user.objects.get(email=email)
        if CHECKUSER.otp == int(otp):
            if npassword == cpassword:
                CHECKUSER.password = npassword
                CHECKUSER.save()
                messages.success(request, "Password updated sucessful")
                return redirect('loginView')
        else:
            messages.error(request, "Wrong OTP!!!")
            return render(request, 'otpVerify.html', {'email':email})
    else:
        return redirect('loginView')

def stationsView(request):
    stations = policeStation.objects.all()
    context = {
        'stations':stations,
    }
    return render(request, 'pstation.html', context)

def servicesView(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['message']
        new_complaint = complaint.objects.create(
            user_id_id = 2,
            title = title,
            complaint_msg = content
        )
        new_complaint.save()
        complaints = complaint.objects.all()
        context = {
            'complaints':complaints
        }
        return render(request, 'services.html', context)
    else:
        complaints = complaint.objects.all()
        context = {
            'complaints':complaints
        }
        return render(request, 'services.html', context)

def deleteComp(request, id):
    getComp = complaint.objects.get(id=id)
    getComp.delete()
    complaints = complaint.objects.all()
    context = {
        'complaints':complaints
    }
    messages.success(request, "Complaint deleted")
    return render(request, 'services.html', context)

def editComp(request, id):
    if request.POST:
        title = request.POST['title']
        content = request.POST['content']
        getComp = complaint.objects.get(id = id)
        if getComp:
            getComp.title = title
            getComp.complaint_msg = content
            getComp.save()
            messages.success(request, "Complaint updated")
            return redirect('servicesView')
    else:
        getComp = complaint.objects.get(id=id)
        return render(request, 'editservice.html', {'getComp':getComp})

def aboutView(request):
    emerg = emergency.objects.all()
    context = {
        'emerg': emerg
    }
    return render(request, 'about.html', context)


def profileView(request):
    if request.session['user_id']:
        id = request.session['user_id']
        user_data = user.objects.get(id=id)
        return render(request, 'profile.html', {'user': user_data})
    else:
        return render(request, 'login.html')


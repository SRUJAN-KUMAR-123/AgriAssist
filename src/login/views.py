from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import CustomUser
from django.utils.dateparse import parse_date
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages





def index_page(request, *args, **kwargs):
    
    
    return render(request, "index.html")

def selectUser_page(request, *args, **kwargs):
    
    
    return render(request, "usertype.html")

def login_page(request, *args, **kwargs):
    
    
    return render(request, "login.html")

def farmerRegistration(request, *args, **kwargs):
    
    
    return render(request, "registration.html")

def userRegistration(request, *args, **kwargs):
    
    
    return render(request, "userregister.html")

def createUser(request, *args, **kwargs):
    
    if request.method == "POST":
        name = request.POST.get("fname")
        usertype = request.POST.get("usertype")
        dob = request.POST.get("dob")
        dob = parse_date(dob)
        mobile = request.POST.get("mobile")
        gender = request.POST.get("gender")
        nationality = request.POST.get("nationality")
        soilType = request.POST.get("soiltype")
        businesstype = request.POST.get("businesstype")
        primarycrops = request.POST.get("pcrops")
        primarypurpose = request.POST.get("primarypurpose")
        farmownership = request.POST.get("farmownership")
        language = request.POST.get("language")
        village = request.POST.get("village")
        state = request.POST.get("state")
        pin = request.POST.get("pin")
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        
        user = CustomUser.objects.create(usertype=usertype, name=name, dob=dob, mobile=mobile, gender=gender, nationality=nationality, soilType=soilType, primaryCrops=primarycrops, 
                                   ownership=farmownership, businessType=businesstype, primaryPurpose=primarypurpose, language=language, town=village, state=state, pincode=pin, uname=uname ,email=email)
        user.set_password( raw_password=password)
        user.save()
        return redirect("/")
    else:
        return render(request, "usertype.html")
    
def login_validation(request, *args, **kwargs):
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(email=email, password=password) 
        
        if user :
            login(request, user)
            return redirect("/")
        else :
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')
        
    else:
        
        return redirect("login.html")
        

def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return HttpResponse(status=404)


def dashboard(request):
    return render(request, "dashboard.html")
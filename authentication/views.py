from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fisrt_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']
       
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('registration')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('registration')
     
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('registration')
        

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('registration')

        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('registration')
    
    
       
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.phone = phone
        
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('takephoto')

    param= {
        "user": 'System Drona',
        'currPage': 'Registration'
    }
    return render(request, 'reg.html', param)

def takephoto(request):
    param= {
        "user": 'System Drona',
        'currPage': 'Registration/ Takephoto'
    }
    return render(request, 'takephoto.html', param)

def singin(request):
    param= {
        "user": 'System Drona',
        'currPage': 'Sing In'
    }
    return render(request, 'singin.html', param)

def singinform(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        print(username)
        print(pass1)
        user = authenticate(username=username, pass1=pass1)
        
        print(user)
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "about.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect("/student")

    param= {
        "user": 'System Drona',
        'currPage': 'Sing In-form'
    }
    return render(request, 'singinform.html', param)


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect("/")
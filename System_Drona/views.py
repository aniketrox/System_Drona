from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contactus(request):
    param= {
        "user": 'System Drona',
        'currPage': 'Contact Us'
    }
    return render(request, 'contactus.html', param)

def about(request):
    param= {
        "user": 'System Drona',
        'currPage': 'About'
    }
    return render(request, 'about.html', param)

def registration(request):
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
    param= {
        "user": 'System Drona',
        'currPage': 'Sing In-form'
    }
    return render(request, 'singinform.html', param)
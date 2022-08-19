from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contactus(request):
    param= {
        "user": 'EMD',
        'currPage': 'Contact Us'
    }
    return render(request, 'contactus.html', param)

def about(request):
    param= {
        "user": 'EMD',
        'currPage': 'About'
    }
    return render(request, 'about.html', param)

def singin(request):
    param= {
        "user": 'EMD',
        'currPage': 'Sing In'
    }
    return render(request, 'singin.html', param)

def singinform(request):
    param= {
        "user": 'EMD',
        'currPage': 'Sing In-form'
    }
    return render(request, 'singinform.html', param)
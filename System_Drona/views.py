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

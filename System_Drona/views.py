from django.shortcuts import render
from subprocess import run,PIPE
import sys

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


def take_sample(request):
    print("click")
    run([sys.executable,"train_test.py"],shell=False,stdout=PIPE)
    return render(request,"singinform.html")

def face_reognition(request):
    print("click")
    run([sys.executable,"face_recognition.py"],shell=False,stdout=PIPE)
    return render(request,"student/exam.html")


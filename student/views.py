from django.shortcuts import render

# Create your views here.
def dashbord(req):
    param= {
        "user": 'Student',
        'currPage': 'Dashbord'
    }
    return render(req, 'student/dashbord.html', param)

def exam(req):
    param= {
        "user": 'Student',
        'currPage': 'Chooose Exam'
    }
    return render(req, 'student/exam.html', param)

def onlineexam(req):
    param= {
        "user": 'Student',
        'currPage': 'Online Exam'
    }
    return render(req, 'student/onlineexam.html', param)

def admitcard(req):
    param= {
        "user": 'Student',
        'currPage': 'Admit Card'
    }
    return render(req, 'student/admitcard.html', param)

def growchart(req):
    param= {
        "user": 'Student',
        'currPage': 'Grow Chart'
    }
    return render(req, 'student/growchart.html', param)

def marpoint(req):
    param= {
        "user": 'Student',
        'currPage': 'Mar Point'
    }
    return render(req, 'student/marpoint.html', param)

def moocspoint(req):
    param= {
        "user": 'Student',
        'currPage': 'Moocs Point'
    }
    return render(req, 'student/moocspoint.html', param)

def reviewresult(req):
    param= {
        "user": 'Student',
        'currPage': 'Review Result'
    }
    return render(req, 'student/reviewresult.html', param)

def updateaccount(req):
    param= {
        "user": 'Student',
        'currPage': 'Update Account'
    }
    return render(req, 'student/updateaccount.html', param)

def account(req):
    param= {
        "user": 'Student',
        'currPage': 'Account'
    }
    return render(req, 'student/account.html', param)

def contactus(req):
    param= {
        "user": 'Student',
        'currPage': 'Contact Us'
    }
    return render(req, 'contactus.html', param)

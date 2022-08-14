from django.shortcuts import render

# Create your views here.
def dashbord(req):
    param= {
        "user": 'Teacher',
        'currPage': 'dashbord'
    }
    return render(req, 'teacher/dashbord.html', param)
def uploadquestion(req):
    param= {
        "user": 'Teacher',
        'currPage': 'Upload Question'
    }
    return render(req, 'teacher/uploadquestion.html', param)

def admitcard(req):
    param= {
        "user": 'Teacher',
        'currPage': 'Admit Card'
    }
    return render(req, 'teacher/admitcard.html', param)

def growchart(req):
    param= {
        "user": 'Teacher',
        'currPage': 'Grow Chart'
    }
    return render(req, 'teacher/growchart.html', param)

def marpoint(req):
    param= {
        "user": 'Teacher',
        'currPage': 'Mar Point'
    }
    return render(req, 'teacher/marpoint.html', param)

def moocspoint(req):
    param= {
        "user": 'Teacher',
        'currPage': 'Moocs Point'
    }
    return render(req, 'teacher/moocspoint.html', param)

def reviewresult(req):
    param= {
        "user": 'Teacher',
        'currPage': 'Review Result'
    }
    return render(req, 'teacher/reviewresult.html', param)

def updateaccount(req):
    param= {
        "user": 'Teacher',
        'currPage': 'Update Account'
    }
    return render(req, 'teacher/updateaccount.html', param)

def account(req):
    param= {
        "user": 'Teacher',
        'currPage': 'Account'
    }
    return render(req, 'teacher/account.html', param)

def contactus(req):
    param= {
        "user": 'Teacher',
        'currPage': 'Contact Us'
    }
    return render(req, 'contactus.html', param)

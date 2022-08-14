from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashbord, name='dashbord'),
    path('dashbord', views.dashbord, name='dashbord'),
    path('exam', views.exam, name='exam'),
    path('onlineexam', views.onlineexam, name='onlineexam'),
    path('admitcard', views.admitcard, name='admitcard'),
    path('growchart', views.growchart, name='growchart'),
    path('marpoint', views.marpoint, name='marpoint'),
    path('moocspoint', views.moocspoint, name='moocspoint'),
    path('reviewresult', views.reviewresult, name='reviewresult'),
    path('updateaccount', views.updateaccount, name='updateaccount'),
    path('account', views.account, name='account'),
    path('contactus', views.contactus, name='dashbord'), 
]
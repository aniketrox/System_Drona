from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.singin, name='singin'),
    path('registration', views.registration, name='registration'),
    path('takephoto', views.takephoto, name='takephoto'),
    path('singinform', views.singinform, name='singinform'),
    path('signout', views.signout, name='signout'),
]
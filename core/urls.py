from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name='index'),
    path("plogin",plogin,name='plogin'),
    path("psignup",psignup,name='psignup'),
    path("dlogin",dlogin,name='dlogin'),
    path("dig",dig,name='dig'),

    path("logout",logout,name='logout'),
    path("result/<int:id>",result,name='result'),
    path("pat",patients,name='pat')
]
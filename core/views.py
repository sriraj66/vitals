from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate


def index(request):
    context = {}
    return render(request, 'core/index.html', context)


def plogin(request):
    context = {}

    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.profile.desg == 'PATIENT':
                return redirect('dig')
            else:
                return redirect('dlogin')
    return render(request, 'core/plogin.html', context=context)


def psignup(request):
    context = {}

    return render(request, 'core/psignup.html', context=context)


def dlogin(request):
    context = {}
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.profile.desg == 'DOCTOR':
                return redirect('pat')
            else:
                return redirect('plogin')
    return render(request, 'core/dlogin.html', context=context)


def vit(bp,sp,bt,pr):
    lev = []
    if bt < 35:
        lev.append(3)
    elif bt < 36:
        lev.append(1)
    elif bt <= 37.9:
        lev.append(0)
    elif bt < 39:
        lev.append(1)
    else:
        lev.append(2)
    
    if sp<85:
        lev.append(3)
    elif sp<92:
        lev.append(2)
    elif sp>92:
        lev.append(0)
    else:
        lev.append(0)

    if pr<40:
        lev.append(2)
    elif pr<=50:
        lev.append(1)
    elif pr<=100:
        lev.append(0)
    elif pr<=110:
        lev.append(1)
    elif pr <= 130:
        lev.append(2)
    else:
        lev.append(3)
    
    if bp<70 or bp>200:
        lev.append(3)
    elif bp<=90 or (bp>170 and bp<=200):
        lev.append(2)
    elif bp >=91 and bp <=170:
        lev.append(0)
    else:
        lev.append(0)
    cm = sum(lev)

    if cm>=7:
        n=3
    elif cm<4 or cm>1:
        n=1
    elif cm==0:
        n=0
    else:
        n=2

    return (cm,n)

def dig(request):
    context = {}
    if request.POST:
        bp = int(request.POST.get('bp'))
        spo2 = int(request.POST.get('spo2'))
        bt = float(request.POST.get('bt'))
        pr = int(request.POST.get('pr'))
        user = request.user

        cm,cl = vit(bp=bp,sp=spo2,bt=bt,pr=pr)
    
        
        obj = Vitals(bp=bp,spo2=spo2,bt=bt,pr=pr,user=user,cl=LEVEL[cl][0],cm=cm)
        obj.save()
        return redirect('result',obj.id)

    return render(request, 'core/dig.html', context=context)

def result(request,id):
    context = {
        "obj" : Vitals.objects.get(id=id)
    }
    n = Vitals.objects.get(id=id)
    cl = n.cl
    
    if cl == 'LOW':
        context['HC']='GOOD'
        context['REC'] = 'NORMAL'
    elif cl == 'HIGH':
        context['HC'] = 'POOR'
        context['REC'] = 'Medical Care is Need'

    elif cl == 'MEDIUM':
        context['HC'] = 'NORMAL'
        context['REC'] = 'Take Care, Good!!'

    else:
        context['HC'] = 'NONE'
        context['REC'] = 'NONE'

    
    return render(request,'core/result.html',context)


def patients(request):
    context = {
        "pat":Vitals.objects.all()
    }
    return render(request,'core/patients.html',context)
def logout(request):
    logout(request)
    return redirect('index')

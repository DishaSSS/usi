from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
import json
from .scrape import attendance, verify
from .forms import AttendForm, SignIn
from .gen import decrypt, encrypt
from .moodle_sel import moodle, assign, mood_verify
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from datetime import datetime
import glob
import random
import os
# Create your views here.


def index(request):
    return render(request, 'landing.html')
def login(request):

        user = User(username=request.session['username'].lower(),
                    password=request.session['password'],
                    regid = request.session['regid'],
                    passw = request.session['passw'],
                    mood_reg = request.session['mood_reg'],
                    mood_passw = request.session['mood_passw'],
                     )
        hour = datetime.now().hour
        name = []
        if hour >=6 and hour <12:
            loc = glob.glob('static/site/morning*.jpg')
        elif 12 <= hour <17:
            loc = glob.glob('static/site/afternoon*.jpg')
        elif 17 <= hour <=20:
            loc = glob.glob('static/site/evening*.jpg')
        elif 20 <= hour <=24:
            loc = glob.glob('static/site/night*.jpg')
        elif 0 <= hour <=6:
            loc = glob.glob('static/site/night*.jpg')
        print(loc)
        loc = random.choice(loc)
        print(location)
        if user not in User.objects.all():
            user.save()
        return HttpResponse(render(request, 'login.html',{'location',loc}))
def signin(request):
    incorrect = False
    hour = datetime.now().hour
    loc = []
    hour = 6
    if hour >=6 and hour <12:
        loc = glob.glob('login/static/site/morning*.jpg')
    elif 12 <= hour <17:

        loc = glob.glob('login/static/site/morning*.jpg')

    elif 17 <= hour <=20:
        loc = glob.glob('login/static/site/evening*.jpg')
    elif 20 <= hour <=24:
        loc = glob.glob('login/static/site/night*.jpg')
        print('hello', hour)
    elif 0 <= hour <=6:
        loc = glob.glob('login/static/site/night*.jpg')
    else:
        loc = glob.glob('*')


    loc = random.choice(loc)
    print(hour, loc)
    if request.method == 'POST':
        form = SignIn(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if User.objects.filter(username=data['username'].lower()) and User.objects.filter(password=data['password']):
                print(User._meta.db_table)
                user = User.objects.filter(username=data['username'].lower())[0]
                request.session['regid']=user.regid
                request.session['passw']=user.passw
                request.session['mood_reg']=user.mood_reg
                request.session['mood_passw']=user.mood_passw
                return render(request,'login.html', {'location': os.path.basename(loc)})
            else:
                incorrect = True
    else:
        form = AttendForm()

    return render(request, 'signin.html', {'form': form, 'incorrect' : incorrect})

def get_name(request):
    # if this is a POST request we need to process the form data
    global check
    check="YES"
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AttendForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = form.cleaned_data
            request.session['regid']=data['regid']
            request.session['passw']=data['passw']
            request.session['mood_reg']=data['mood_reg']
            request.session['mood_passw']=data['mood_passw']
            request.session['username'] = data['username']
            request.session['password'] = data['password']
            return HttpResponseRedirect('login/',request)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AttendForm()

    return render(request, 'attend.html', {'form': form})
@csrf_exempt
def apiassignment(request):
        return JsonResponse(assign(request.POST["hr"],request.POST["mood_reg"],request.POST["mood_passw"]), safe=False)
@csrf_exempt
def apiattend(request):
    if request.method=='POST':
        dic = attendance(request.POST['regid'], request.POST['passw'])
    else:
        dic = None
    return JsonResponse(dic, safe=False)

@csrf_exempt
def apimoodle(request):
    if request.method == 'POST':
        dic = moodle(request.POST['mood_reg'],request.POST['mood_passw'])
    else:
        dic = None
    return JsonResponse(dic,safe=False)
@csrf_exempt
def apidown(request):
    if request.method == 'POST':
        pass
@csrf_exempt
def verify_moodle(request):
    if request.method == 'POST':
        print(request.POST['mood_reg'],request.POST['mood_passw'])
        return JsonResponse({'STATUS':mood_verify(request.POST['mood_reg'],request.POST['mood_passw'])}, safe=False)
    else:
        return JsonResponse(None,safe=False)
@csrf_exempt
def verify_erp(request):
    if request.method=='POST':
        return JsonResponse({'STATUS':verify(request.POST['regid'],request.POST['passw'])}, safe=False)
    else:
        return JsonResponse(None,safe=False)
@csrf_exempt
def check_user(request):
    print(User.objects.all(), request.POST['username'])
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username'].lower()):
            return JsonResponse({'match':True}, safe=False)
        else:
            return JsonResponse({'match':False}, safe=False)

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from mainapp.models import Account, Profile
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

import datetime as D


appname = 'Dating App'

def index(request):
    context = { 'appname': appname }
    return render(request,'mainapp/index.html',context)

def messages(request):
    context = { 'appname': appname }
    return render(request,'mainapp/messages.html',context)

def signup(request):
    context = { 'appname': appname }
    return render(request,'mainapp/signup.html',context)

def login(request):
    context = { 'appname': appname }
    return render(request,'mainapp/login.html',context)

def loggedin(view):
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try: user = Account.objects.get(username=username)
            except Account.DoesNotExist: raise Http404('Account does not exist')
            return view(request, user)
        else:
            return render(request,'mainapp/not-logged-in.html',{})
    return mod_view

def register(request):
    if 'username' in request.POST and 'password' in request.POST:
        u = request.POST['username']
        p = request.POST['password']
        user = Account(username=u)
        user.set_password(p)
        try: user.save()
        except IntegrityError: raise Http404('Username '+u+' already taken: Usernames must be unique')
        context = {
            'appname' : appname,
            'username' : u
        }
        return render(request,'mainapp/user-registered.html',context)

    else:
        raise Http404('POST data missing')

def checkuser(request):
    if 'username' in request.POST:
        try:
            account = Account.objects.get(username=request.POST['username'])
        except Account.DoesNotExist:
            if request.POST['page'] == 'login':
                return HttpResponse("<span class='taken'>&nbsp;&#x2718; Invalid username</span>")
            if request.POST['page'] == 'register':
                return HttpResponse("<span class='available'>&nbsp;&#x2714; This username is available</span>")
    if request.POST['page'] == 'login':
        return HttpResponse("<span class='available'>&nbsp;&#x2714; Valid username</span>")
    if request.POST['page'] == 'register':
        return HttpResponse("<span class='taken'>&nbsp;&#x2718; This username is taken</span>")
    return HttpResponse("<span class='taken'>&nbsp;&#x2718; Invalid request</span>")

def login(request):
    if not ('username' in request.POST and 'password' in request.POST):
        context = { 'appname': appname }
        return render(request,'mainapp/login.html',context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        try: account = Account.objects.get(username=username)
        except Account.DoesNotExist: raise Http404('User does not exist')
        if account.check_password(password):
            # remember user in session variable
            request.session['username'] = username
            request.session['password'] = password
            context = {
               'appname': appname,
               'username': username,
               'loggedin': True
            }
            response = render(request, 'mainapp/login.html', context)
            # remember last login in cookie
            now = D.datetime.utcnow()
            max_age = 365 * 24 * 60 * 60  #one year
            delta = now + D.timedelta(seconds=max_age)
            format = "%a, %d-%b-%Y %H:%M:%S GMT"
            expires = D.datetime.strftime(delta, format)
            response.set_cookie('last_login',now,expires=expires)
            return response
        else:
            raise Http404('Wrong password')

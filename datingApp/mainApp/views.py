from django.shortcuts import render
from django.http import HttpResponse
from mainapp.templatetags.extras import display_message

# datetime library to get time for setting cookie
import datetime as D
import sys

appname = 'mainApp'

def index(request):
    

# decorator that tests whether user is logged in
def loggedin(view):
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try: user = Member.objects.get(username=username)
            except Member.DoesNotExist: raise Http404('Member does not exist')
            return view(request, user)
        else:
            return render(request,'mainApp/nologin.html',{})
    return mod_view

def index(request):
    context = { 'appname': appname }
    return render(request,'mainApp/index.html',context)

def signup(request):
    context = { 'appname': appname }
    return render(request,'mainApp/signup.html',context)

def register(request):
    if 'username' in request.POST and 'password' in request.POST:
        u = request.POST['username']
        p = request.POST['password']
        user = Member(username=u)
        user.set_password(p)
        try: user.save()
        except IntegrityError: raise Http404('Username '+u+' already taken: Usernames must be unique')
        context = {
            'appname' : appname,
            'username' : u
        }
        return render(request,'mainApp/user-registered.html',context)

    else:
        raise Http404('POST data missing')

def login(request):
    if not ('username' in request.POST and 'password' in request.POST):
        context = { 'appname': appname }
        return render(request,'mainapp/login.html',context)
    else:
        username = request.POST['username']
        password = request.POST['password']
        try: member = Member.objects.get(username=username)
        except Member.DoesNotExist: raise Http404('User does not exist')
        if member.check_password(password):
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
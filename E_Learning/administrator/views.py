from django.shortcuts import render


from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from administrator.forms import admintrator_login_form
from administrator.models import Administrative_Data
from django.contrib.auth.models import User

# Create your views here.

def admin_login(request):
    authenticated=False
    if(request.method=="POST"):

        login_form=admintrator_login_form(request.POST)
        print("login_form.is_valid()",login_form.is_valid())
        print("login_form.errors",login_form.errors)
        if(login_form.is_valid()):

            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print("username:",username,"password:",password)
            user=authenticate(request,username=username,password=password)

            #---
            #query=Administrative_Data.objects.get(username=username)
            #print("query:",query.username,"query.password",query.password)
            #---

            if user is not None:
                
                username = login_form.cleaned_data['username']
                user_instance=User.objects.get(username=username)
                
                login(request, user)
                print("login")
                return render(request, 'administrator/administrator_page.html', {'username': request.POST.get('username')})

                authenticated=True
            else:
                print("login Failed")
                # Authentication failed
                return render(request, 'administrator/admin_login.html',{'form':admintrator_login_form()})

        login_form=admintrator_login_form()
    else:
        login_form=admintrator_login_form()                

    return render(request,'administrator/admin_login.html',{"form":admintrator_login_form()})

def administrator_page(request):
    return render(request,"administrator/administrator_page.html")

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from teacher_app.forms import Teacher_login_form
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

"""def index(request):
    return render(request,"common/index.html")"""



def teacher_login(request):
    authenticated=False
    #checks if user is already authenticated then user is redirected to users page and not to login page
    if (request.user.is_authenticated): 
        if(request.user.groups.filter(name='Teacher_Group').exists()):
            return redirect('/teacher_app/adminstrator_page/')


    if(request.method=="POST"):

        login_form=Teacher_login_form(request.POST)
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

            if user is not None  and user.groups.filter(name='Teacher_Group').exists():
                
                username = login_form.cleaned_data['username']
                user_instance=User.objects.get(username=username)
                
                login(request, user)
                print("login")
                return render(request, 'teacher/teacher_page.html', {'username': request.POST.get('username')})

                authenticated=True
            else:
                print("login Failed")
                # Authentication failed
                return render(request, 'teacher/login.html',{'form':Teacher_login_form()})

        login_form=Teacher_login_form()
    else:
        login_form=Teacher_login_form()                

    return render(request,'teacher/login.html',{"form":Teacher_login_form()})





def is_teacher(user):
    return user.groups.filter(name='Teacher_Group').exists()

@user_passes_test(is_teacher)
def teacher_page(request):
    return render(request,"teacher/teacher_page.html")


@user_passes_test(is_teacher)
def teacher_logout(request):
    logout(request)
    return redirect("/")
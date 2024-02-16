from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from student_app.forms import Student_login_form
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

#home page 
def index(request):
    return render(request,"common/index.html")


# student login
def student_login(request):
    authenticated=False

    #checks if user is already authenticated then user is redirected to users page and not to login page
    if (request.user.is_authenticated):
        if(request.user.groups.filter(name='Student_Group').exists()):
            return redirect("/student_app/student_page/")

    if(request.method=="POST"):

        login_form=Student_login_form(request.POST)
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

            if user is not None  and user.groups.filter(name='Student_Group').exists():
                
                username = login_form.cleaned_data['username']
                user_instance=User.objects.get(username=username)
                
                login(request, user)
                print("login")
                #return render(request, 'student/student_page.html', {'username': request.POST.get('username')})
                return redirect("/student_app/student_page/")

                authenticated=True
            else:
                print("login Failed")
                # Authentication failed
                return render(request, 'student/login.html',{'form':Student_login_form()})

        login_form=Student_login_form()
    else:
        login_form=Student_login_form()                

    return render(request,'student/login.html',{"form":Student_login_form()})


#checks if user belongs to Student_group
def is_student(user):
    return user.groups.filter(name='Student_Group').exists()

#page is restricted only to Student_group
@user_passes_test(is_student)
def student_page(request):
    return render(request,"student/student_page.html")

#logout student
@user_passes_test(is_student)
def student_logout(request):
    logout(request)
    return redirect("/")
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from administrator.forms import admintrator_login_form
from administrator.models import Administrative_Data
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group
# Create your views here.
from django.contrib.auth.decorators import user_passes_test

#group_dict={"Teacher_Group":"Teacher_Group","Student_Group":"Student_Group","Administrator_Group":"Administrator_Group"}


def admin_login(request):
    authenticated=False

    if(request.user.is_authenticated):
        if(request.user.groups.filter(name='Administrator_Group').exists()):#problem here
            return redirect('/administrator/administrator_page/')

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
            print("request.user.groups.filter(name='Administrator_Group').exists():",user.groups.filter(name='Administrator_Group').exists())
            if (user is not None and user.groups.filter(name='Administrator_Group').exists()):
                
                username = login_form.cleaned_data['username']
                user_instance=User.objects.get(username=username)
                
                login(request, user)
                print("login")
                #return render(request, 'administrator/administrator_page.html', {'username': request.POST.get('username')})
                #administrator/adminstrator_page/
                return redirect('/administrator/administrator_page/')
                #return redirect(reverse("administrator_page"))
                authenticated=True
            else:
                print("login Failed")
                # Authentication failed
                return render(request, 'administrator/admin_login.html',{'form':admintrator_login_form()})

        login_form=admintrator_login_form()
    else:
        login_form=admintrator_login_form()                

    return render(request,'administrator/admin_login.html',{"form":admintrator_login_form()})

def is_administrator(user):
    return user.groups.filter(name='Administrator_Group').exists()

@user_passes_test(is_administrator)
def admin_logout(request):
    logout(request)
    return redirect("/")

@user_passes_test(is_administrator)
def administrator_page(request):
    return render(request,"administrator/administrator_page.html")


#function to add a user to a group
@user_passes_test(is_administrator)
def add_user_to_group(username, group_name):

    #1 Retrieve the User
    #2 Retrieve the Group
    #3 Add User to Group
    try:
        user = User.objects.get(username=username)
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        print(f"User '{username}' added to group '{group_name}' successfully.")
    except User.DoesNotExist:
        print(f"User '{username}' does not exist.")
    except Group.DoesNotExist:
        print(f"Group '{group_name}' does not exist.")


@user_passes_test(is_administrator)
def administrator_add_student(request):
    return render(request,"administrator/add_student.html")

@user_passes_test(is_administrator)
def administrator_add_teacher(request):
    return render(request,"administrator/add_teacher.html")
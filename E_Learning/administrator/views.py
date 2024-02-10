from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from administrator.forms import admintrator_login_form
from django.contrib.auth.models import User
from django.contrib.auth.models import User, Group
import pandas as pd
import numpy as np
from django.contrib.auth.decorators import user_passes_test
#from django.contrib.auth import make_random_password
from django.http import JsonResponse
from teacher_app.models import Teacher_details
from E_Learning.settings import BASE_DIR
import secrets
import string
from pathlib import Path



#group_dict={"Teacher_Group":"Teacher_Group","Student_Group":"Student_Group","Administrator_Group":"Administrator_Group"}
df=""

def admin_login(request):
    authenticated=False

    #checks if user is already authenticated then user is redirected to users page and not to login page
    if(request.user.is_authenticated):
        if(request.user.groups.filter(name='Administrator_Group').exists()):
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

@user_passes_test(is_administrator)
def file_upload_success(request):
    #display the excel content in a tabular form
    global df
    df_user_created=df[df['user_created']==True]
    df_user_not_created=df[df['user_created']==False]

    dict_df_user_created=df_user_created.to_dict(orient='records')
    dict_df_user_not_created=df_user_not_created.to_dict(orient='records')

    
    """for index,row in df.iterrows():
        if(row["user_created"]==True):
            data={"teacher_first_name":row["teacher_first_name"],
                      "teacher_last_name":row["teacher_last_name"],
                      "teacher_dob":row["teacher_dob"],
                      "teacher_sex":row["teacher_sex"],
                      "teacher_email":row["teacher_email"],
                      "teacher_mobile":row["teacher_mobile"]
                      }
    """           
    
    return render(request,"administrator/upload_success.html",{"dict_df_user_created":dict_df_user_created,"dict_df_user_not_created":dict_df_user_not_created})

@user_passes_test(is_administrator)
def file_upload(request):
    global df
    if request.method=="POST" and request.FILES['file']:
        upload_file=request.FILES['file']
        
        try:
            

            #first try to save the data
            file_path='media/administrator/' + upload_file.name
            with open('media/administrator/' + upload_file.name, 'wb+') as destination:
                for chunk in upload_file.chunks():
                    destination.write(chunk)
            print(file_path)

            
            #read the data from file
            print(type(df))
            
            #abs_file_path=BASE_DIR+file_path
            abs_file_path=Path.joinpath(BASE_DIR,file_path)
            print(abs_file_path)
            #df=pd.read_excel(upload_file,sheet_name="Sheet1")
            df=pd.read_excel(abs_file_path)
            print("debug")

            df['user_created'] = False
            df['username']=np.nan
            df["password"]=np.nan
            
            for index,row in df.iterrows():
                #create username from first and last name
                #check if the username already exixts in users list if already present add a no at the end
                username=row["teacher_first_name"]+row["teacher_last_name"]
                username_new=username
                num=0
                while(True):
                        
                    if(User.objects.filter(username=username_new).count()>0):
                        username_new=username+str(num)
                        num+=1
                    else:
                        break
                print("username_new",username_new)
                #password=make_random_password(size=8)
                alphabet = string.ascii_letters + string.digits
                password=''.join(secrets.choice(alphabet) for i in range(8))
                user_data={
                    "username":username_new,
                    "password":password,
                }

                df.at[index,"username"]=username_new
                df.at[index,"password"]=password

                user=User.objects.create(**user_data)
                print("line191")
                data={
                    "user":user,
                    "teacher_first_name":row["teacher_first_name"],
                    "teacher_last_name":row["teacher_last_name"],
                    "teacher_dob":row["teacher_dob"],
                    "teacher_sex":row["teacher_sex"],
                    "teacher_email":row["teacher_email"],
                    "teacher_mobile":row["teacher_mobile"]      
                      }

                
                Teacher_details.objects.create(**data)
                df["user_created"]=True
                group = Group.objects.get(name='Teacher_Group')
                group.user_set.add(user)
                #user.groups.add(name=group)
                print("df.head()",df.head())
            return JsonResponse({'message': 'File uploaded successfully'}, status=200)

        except Exception as e:
            print(e)
            df=""
            return JsonResponse({'error': 'No file was uploaded'}, status=400)
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'E_Learning.settings')
django.setup()


from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User

def create_group():
    
    teacher_group_ins,created=Group.objects.get_or_create(name="Teacher_Group")
    if created:
        print("Teacher Group Created")
    else:
        print("Teacher Group Existed")

    student_group_ins,created=Group.objects.get_or_create(name="Student_Group")
    if created:
        print("Student Group Created")
    else:
        print("Student Group Existed")

    administrator_group_ins,created=Group.objects.get_or_create(name="Administrator_Group")
    if created:
        print("Administrator Group Created")
    else:
        print("Administrator Group Existed")
    
    #teacher_model="Teacher_details"
    teacher_permissions=["Can view teacher_details","Can view student_details","Can change student_details","Can change teacher_details",]
    for per in teacher_permissions:
        try:
            model_add_perm = Permission.objects.get(name=per)
            teacher_group_ins.permissions.add(model_add_perm)
        except Permission.DoesNotExist:
            print("permission Does not Exists:",per)
            continue
        
        


    #student_model="Student_details"
    student_permissions=["Can view student_details","Can change student_details"]

    for per in student_permissions:
        try:
            model_add_perm = Permission.objects.get(name=per)
            student_group_ins.permissions.add(model_add_perm)
        except Permission.DoesNotExist:
            print("permission Does not Exists:",per)
            continue



    administrator_permissions=["Can view teacher_details","Can add teacher_details","Can delete teacher_details","Can change teacher_details",
                               "Can view student_details","Can add student_details","Can delete student_details","Can change student_details",
                               "Can view administrative_ data",
                               ]
    for per in administrator_permissions:
        try:
            model_add_perm = Permission.objects.get(name=per)
            administrator_group_ins.permissions.add(model_add_perm)
        except Permission.DoesNotExist:
            print("permission Does not Exists:",per)
            continue
        
        

if __name__=="__main__":
    create_group()

from django.urls import path,include
from administrator import views

app_name='administrator'
urlpatterns = [
    path('administrator_login/',views.admin_login,name="administrator_login"),
    path('administrator_logout/',views.admin_logout,name="administrator_logout"),
    path('administrator_page/',views.administrator_page,name="administrator_page"),
    path('add_student/',views.administrator_add_student,name="add_student"),
    path('add_teacher/',views.administrator_add_teacher,name="add_teacher"),
    path("administrator_upload_success_teacher/",views.file_upload_success_teacher,name="file_upload_success_teacher"),
    path("administrator_upload_teacher_excel/",views.excel_file_upload_teacher,name="upload_teacher_file"),
    path("administrator_upload_student_excel/",views.excel_file_upload_student,name="upload_student_file"),
    path("administrator_upload_success_student/",views.file_upload_success_student,name="file_upload_success_student")
    
]
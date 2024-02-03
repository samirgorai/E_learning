from django.urls import path
from student_app import views

app_name='student_app'
urlpatterns = [
    path('login/',views.student_login,name="student_login"),
    path('adminstrator_page/',views.student_page,name="student_page"),
]

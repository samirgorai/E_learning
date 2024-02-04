from django.urls import path
from teacher_app import views

app_name='teacher_app'
urlpatterns = [
    path('login/',views.teacher_login,name="teacher_login"),
    path('teacher_logout/',views.teacher_logout,name="teacher_logout"),
    path('adminstrator_page/',views.teacher_page,name="teacher_page"),
]


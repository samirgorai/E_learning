
from django.urls import path,include
from administrator import views

app_name='administrator'
urlpatterns = [
    path('login/',views.admin_login,name="administrator_login"),
    path('adminstrator_page/',views.administrator_page,name="administrator_page"),
]

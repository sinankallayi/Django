from . import views
from django.urls import path,include

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("department",views.department_view,name="department"),
    path("booking",views.booking,name="booking"),
    path("register",views.register_view,name="register"),
    path("login",views.login_view,name="login"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("student",views.student,name="student"),
    path("add-student/",views.add_student,name="add-student"),
    
]
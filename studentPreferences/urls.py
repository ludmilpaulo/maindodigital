from django.urls import path
from . import views

app_name = 'studentPreferences'
urlpatterns = [
    path('',views.index,name = "email-student-pref"),
    path('change-password/',views.change_password,name="change_password"),
]
